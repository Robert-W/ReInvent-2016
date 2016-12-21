Second Keynote
==============

#### Notes
* Twilio CEO said they deploy 8000 times a year, approximately 30 times a day, and have 99.999% availability.
* Best practices for transformational development
	* Look at something called "The Twelve-Factor App"
* Automation
	* If you can integrate automation as much as possible, you can increase security, reliability, and efficiency.
* Well architected framework
> Look into the Well-Architected Framework Course

	* Security
	* Reliability
	* Performance efficiency
	* Cost optimization
	* Operational excellence
		* Prepare
			* Checklists
			* Operator actions (Automation targets escalations)
			* Environments (Dev-Test-Deploy)
		* Operate
			* Continuous delivery (CI/CD)
				* Source -> Build -> (Staging/Pre-production/Production)
				* See CodeBuild below
			* Monitoring
				* CloudWatch metrics, events, logs
				* CloudTail
		* Respond
			* Playbook
			* Real-time alarming
			* Automated responses
			* Automated escalation paths
* Cloud Formation
	* 20 new services
	* 20 services updated
	* YAML support
	* Role based stack creation
	* Change sets
	* Cross-stack references
	* Failure recovery
	* Resource schemas
* Trainline open sourced their [environment manager](https://github.com/trainline/environment-manager) tool on Github
* Amazon Redshift
	* Garbage collection and performance upgrades
* Amazon QuickSight
	* Great for business intelligence
* Three core principles from Chief data scientist for the white house
	* People are always greater than data (People >> Data)
	* Data is a force multiplier
	* The time to engage is now
* Steps to successful Analytics (All steps can now be completed with the new AWS Glue)
	* Automated Ingestion
		* S3 Upload or Accelerate, Kinesis, Dynamo Streams
	* Preservation of original source data
		* Should consider making it immutable
		* S3, DyanmoDB, RDS, EFS, EBS
	* Lifecycle management and cold storage
		* S3 Storage Management, Glacier
	* Capture metadata
	* Managing governance, security, and privacy
		* Classify data
		* KMS, Config, CLoudTrail
	* Self service discovery, search, and access
	* Managing data quality, garbage in is garbage out
		* EMR
	* Preparing for analytics
	* Orchestration & Job Scheduling
	* Capturing data changes
* Spectrum of Compute
	* Virtual Machines
	* Containers
	* Serverless

#### New
* **AWS OpsWorks for Chef Automate**
	* Managed chef server
* **Amazon EC2 Systems Manager**
	* Collection of AWS tools for package installation, patching, service configuration, and task automation
* **AWS CodeBuild**
	* Fully managed build service for compiling code and running tests
	* Pay per minute
	* Can be pointed at a docker image and just run it when it's ready
	* Part of AWS CodePipeline
		* AWS CodeCommit
		* AWS CodeBuild
		* AWS CodeDeploy
* **AWS X-Ray**
	* Deeper insight into Application & Service execution
	* Analyze and debug distributed applications in production
	* Distributed graph with deep dive into individual services, latency of individual requests, and much more.
	* See specific timing for services communicating with each other. (e.g. elastic beanstalk took Xms to talk to DynamoDB)
* **AWS Personal Health Dashboard**
	* Personalized view of AWS service health
	* Can add listeners to system events happening within AWS
* **AWS Shield for Everyone**
	* Turned on by default
	* Protects Volumetric, State Exhaustion, and Application layer DDOS attacks
	* Web applications running on AWS all are already using this, automatically
* **AWS Shield Advanced**
	* Additional protection against very large and sophisticated attacks
	* Advanced notifications on CloudWatch
	* Much more
* **Amazon Pinpoint**
	* Understand your users
	* Describe who to target
	* Send out notifications
	* track campaign results
* **S3 Storage management**
	* Data events in CloudTrail
	* Object tagging
	* Analytics - Storage class analytics
	* CloudWatch metrics
	* Inventory
* **AWS Glue**
	* Fully managed data catalog and ETL Service
	* Integrated with S3, RDS, Redshift, DynamoDB, and even databases that are on-premise
	* Build transformations to prepare data for analytics
	* Schedule and run your jobs
* **AWS Batch**
	* Fully managed batch processing at scale
	* Make use of Spot Market
	* Priority based queues and scheduling
	* Fully managed
	* Cost optimized
* **Blox**
	* Collection of open source projects
	* Container management and orchestration
	* Cluster state service, consumes event streams from ECS
	* Daemon-Scheduler
	* blox.github.io

#### Coming Soon
* Task Placement Engine with the following strategies
	* Binpacking
	* Spread
	* Affinity
	* Distinct Instance