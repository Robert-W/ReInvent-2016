Automating Policy Validation
============================

#### Policy Review
* Grants access to what a user can do and with which resources.
* JSON formatted documents
* Contains a simple Statement with Effect, Action, and Resource
* Identity based policies
	* Attached to an IAM User, group, role
* Resource based policies
	* Attached to a resource to specify who has access to the resource
	
#### Policy Structure
* Principle - Entity allowed or denied access to a resource. Required for resource based but not identity based
* Action - Service and actions
* Resource - Objects the actions can be performed on
* Conditions - Conditions for when the statement is in effect

#### Scenarios - When to Validate

##### Actions
* IAM:Put(User, Group, Role) Policy - Updates an inline policy
* S3:PutBucketPolicy - Updates S3 Bucket Policy
* KMS:Decrypt - Decrypts KMS ciphertext

##### Resources
* S3 Buckets - any with sensitive information
* EC2 Instances - runs critical services

### Scenarios to Validate (Three but many more exist)
* Validate who can call powerful actions
* Who's allowed to access a critical resource
* Launch EC2 instances in restricted regions

### Testing your policies
* Use the IAM policy simulator
* API's for Automation
	* IAM:SimulatePrincipalPolicy - Simulate policies attached to user, group, or role to determine effective list of permissions for actions and resources
	* IAM:SimulateCustomPolicy
	
```shell
aws iam simulate-principal-policy --policy-source-arn ...
--action-names ...
```

#### Automation
* AWS Lambda
* AWS Config Rules - Anytime something changes, trigger a lambda
* Amazon SNS

#### Solutions of when to validate
* Periodic Audit
* Configuration Change

#### Solution to Architecture
* AWS Config Rules - When a user, group, role, or policy changes, trigger a Lambda function.
* AWS Lambda - Run policy validation on resources to check if they are compliant
	* Validate Powerful actions
	* Validate critical resources
	* Validate restricted regions
* Amazon SNS - Send email's or notifications when things change with the results from Lambda

#### Core elements of the Lambda Function
* Inputs
	* IAM resource
	* Related resources
	* Resource policies
* Validation
	* Simulate permissions or related entities via the APIs
* Output

#### Helper functions
get users for group
simulate group
evaluate compliance

#### Code samples and slides to be provided