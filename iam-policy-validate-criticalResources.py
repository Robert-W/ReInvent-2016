#This function validates the permissions for users, groups, roles, and policies for the critical resources AWS Config Rule
# Trigger Type: Change Triggered
# Scope of Changes: IAM:User, IAM:Group, IAM:Role, IAM:Polciy

import json
import boto3

# Resource types this function can evaluate
APPLICABLE_RESOURCES = ["AWS::IAM::User", "AWS::IAM::Group","AWS::IAM::Role","AWS::IAM::Policy"]

# Actions non-compliant on a specific resource
ACTIONS = ["s3:GetObject"]

# The critical bucket
BUCKET_ARN = "arn:aws:s3:::aws-reinvent-session-311-hr/*"
BUCKET_NAME = "aws-reinvent-session-311-hr"

def evaluate_compliance(configuration_item, result_token):
    resource_name = configuration_item["resourceName"]
    resource_arn = configuration_item["ARN"]
    timestamp = configuration_item["configurationItemCaptureTime"]
    resource_type = configuration_item["resourceType"]
    resource_id = configuration_item["resourceId"]
    account_id = configuration_item["awsAccountId"]

    # Error out if resource is not applicable
    if resource_type not in APPLICABLE_RESOURCES:
        return "NOT_APPLICABLE"

    # Create clients to call other services
    iam = boto3.client("iam")
    config = boto3.client("config")

    # logic for entity type and simulation
    if resource_type == "AWS::IAM::User" or resource_type == "AWS::IAM::Role":
        compliance_status = simulate_principal_policy(iam, resource_arn, resource_type)
        record_results(config, compliance_status, result_token, resource_type, resource_id, resource_arn, timestamp)
    elif resource_type == "AWS::IAM::Group":
        simulate_group(resource_arn, resource_id, resource_name, config, iam, result_token, timestamp)
    elif resource_type == "AWS::IAM::Policy":
        # Simulate the policy and record it's result
        compliance_status = simulate_managed_policy(iam, resource_arn)
        record_results(config, compliance_status, result_token, resource_type, resource_id, resource_arn, timestamp)

        # Get al attached entities for policy
        attached_entities = iam.list_entities_for_policy(PolicyArn=resource_arn, MaxItems=1000)

        # Simulate all principals
        for role in attached_entities["PolicyRoles"]:
            role_arn = "arn:aws:iam::" + account_id + ":role/" + role["RoleName"]
            compliance_status = simulate_principal_policy(iam, role_arn, "AWS::IAM::Role")
            record_results(config, compliance_status, result_token, "AWS::IAM::Role", role["RoleId"], role_arn, timestamp)
            
        for user in attached_entities["PolicyUsers"]:
            user_arn = "arn:aws:iam::" + account_id + ":user/" + user["UserName"]
            compliance_status = simulate_principal_policy(iam, user_arn, "AWS::IAM::User")
            record_results(config, compliance_status, result_token, "AWS::IAM::User", user["UserId"], user_arn, timestamp)
            
        for group in attached_entities["PolicyGroups"]:
            group_arn = "arn:aws:iam::" + account_id + ":group/" + group["GroupName"]
            simulate_group(group_arn, resource_id, group["GroupName"], config, iam, result_token, timestamp)

def simulate_principal_policy(iam, resource_arn, resource_type):
    # Get the resource-based policy
    bucket_policy=get_bucket_policy()
    
    # Call IAM to simulate the policy on critical resources.
    if(bucket_policy is not None and resource_type == "AWS::IAM::User"):
        response = iam.simulate_principal_policy(PolicySourceArn=resource_arn,ActionNames=ACTIONS,ResourceArns=[BUCKET_ARN],ResourcePolicy=bucket_policy, CallerArn=resource_arn)
    else:
        response = iam.simulate_principal_policy(PolicySourceArn=resource_arn,ActionNames=ACTIONS,ResourceArns=[BUCKET_ARN])
    
    results = response['EvaluationResults']
    allows_critical_resource = False

    # Determine if the simulation allowed access to critical resource.
    for actions in results:
        eval_decision = actions['EvalDecision']
        print "Evaluation Decision for " + resource_arn + " is " + eval_decision

        if(eval_decision == 'allowed'):
            action_name = actions['EvalActionName']
            print "Action " + action_name + " was granted to resource " + resource_arn
            allows_critical_resource = True

    # If any resources were allowed, consider the resource non-compliant.
    if(allows_critical_resource):
        return "NON_COMPLIANT"
    return "COMPLIANT"

def simulate_managed_policy(iam, policy_arn):
    # Retrieve the policy.
    get_policy_response = iam.get_policy(PolicyArn=policy_arn)
    default_version = get_policy_response["Policy"]["DefaultVersionId"]
    get_policy_version_response = iam.get_policy_version(PolicyArn=policy_arn, VersionId=default_version)
    policy_document = json.dumps(get_policy_version_response["PolicyVersion"]["Document"])
    
    # Simulate the policy
    simulation_response = iam.simulate_custom_policy(PolicyInputList=[policy_document], ActionNames=ACTIONS, ResourceArns=[BUCKET_ARN])
    results = simulation_response['EvaluationResults']
    allows_critical_resource = False

    # Determine if any action is allowed on the critical resource.
    for actions in results:
        evalDecision = actions['EvalDecision']

        if(evalDecision == 'allowed'):
            actionName = actions['EvalActionName']
            print "Restricted action " + actionName + " was granted to resource " + policy_arn
            allows_critical_resource = True

    # If any resources were allowed, consider the resource non-compliant.
    if(allows_critical_resource):
        return "NON_COMPLIANT"
    return "COMPLIANT"
    
def record_results(config, compliance_result, result_token, resource_type, resource_id, resource_arn, timestamp):
    # Call Config to record the results of our evaluation.
    annotation = "Entity: " + resource_arn + " is " + compliance_result + " for validation of critical resource access."
    config.put_evaluations(
        Evaluations=[
            {
                "ComplianceResourceType": resource_type,
                "ComplianceResourceId": resource_id,
                "ComplianceType": compliance_result,
                "Annotation": annotation,
                "OrderingTimestamp": timestamp
            },
        ],
        ResultToken=result_token
    )
    
def get_users_for_group(iam, group_name):
    response = iam.get_group(GroupName=group_name, MaxItems=1000)
    user_arns = []
    for user in response["Users"]:
        user_arns.append({'Arn': user["Arn"], 'UserId': user["UserId"]})
    return user_arns
    
def simulate_group(group_arn, group_id, group_name, config, iam, result_token, timestamp):
   # Simulate group, save status
    compliance_status = simulate_principal_policy(iam, group_arn,"AWS::IAM::Group")
    record_results(config, compliance_status, result_token, "AWS::IAM::Group", group_id, group_arn, timestamp)
    
    # Retrieve the ARNs of all users in the group
    users = get_users_for_group(iam, group_name)
    
    # For each user, simulate_principal
    for user in users:
        compliance_status = simulate_principal_policy(iam, user["Arn"], "AWS::IAM::User")
        record_results(config, compliance_status, result_token, "AWS::IAM::User", user["UserId"], user["Arn"], timestamp)

def get_bucket_policy():
    # Call S3 to get a bucket policy
    bucket_policy = None
    try:
        s3 = boto3.client("s3")
        retrieve_policy_result = s3.get_bucket_policy(Bucket=BUCKET_NAME)
        if(retrieve_policy_result is not None):
            bucket_policy = retrieve_policy_result["Policy"]
        print "Bucket policy: " + bucket_policy
    except:
        print "No bucket policy found."
    return bucket_policy

def lambda_handler(event, context):
    invoking_event = json.loads(event["invokingEvent"])
    configuration_item = invoking_event["configurationItem"]
    result_token = "No token found."
    if "resultToken" in event:
        result_token = event["resultToken"]

    # Evaluate whether the resource is compliant
    evaluate_compliance(configuration_item, result_token)