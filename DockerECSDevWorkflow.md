Development Workflow with Docker and ECS
========================================

* Should look into Code Pipeline, aka CodeCommit, CodeBuild, and CodeDeploy.
* This talk had some interesting content around Docker and ECS, may be worth looking up online later.

#### Basics
* Beyond continuous integration, you should have continuous deployment, delivery, and feedback.
* Work towards a micro service architecture
* Docker and Docker Beta
* Use docker-compose, duh
* Build
	* ECS plugin for Jenkins
	* Build artifacts to push image to ECR (EC2 container registry)
	* Registry integrates with CloudTrail and can be regulated by IAM Roles, Integration with Docker, ECS, and backed by S3
	* Run tests with `docker-compose run`
* AWS Elastic Beanstalk can also deploy containers
	* Manages ELB, ECS Cluster, Monitoring, and Logging
	* Docker support is single and multi-container
* Amazon ECS CLI

#### How to use Docker with CI/CD
* Continuous delivery with Jenkins
* See Photo
* Continuous delivery to ECS with CodePipeline
	* Lambda function creates EC2, Jenkins runs and pushes to ECR, Lambda kills the EC2 instance, continue deployment
* Some existent CI can integrate with ECS

#### Okta
* Okta looks like a nice identity platform for developers, they participated in the talk and talked a lot about themselves before getting into their Docker workflow
* Container frameworks
	* Docker is first, almost used Rocket and may switch at some point
* Cluster schedulers	
	* Used ECS, almost chose Kubernetes but felt ECS handled their use case better (no details provided though)
* How they work?
	* 1 Week sprints
	* Biggest repo has 33k tests, takes an hour, tests must pass before merge
* How they ship?
	* Deploy to Prod weekly
* Challenges
	* Developer experience
		* fast turn around time and reliable results
	* Quality
		* Need all tests to run every time
	* Cost
		* Need to run as cheaply as possible
	* Cloud first
		* use cloud services whenever possible
* Requirements for their CI
	* Clean testing environment, parallel tests and serial runs, isolated environments
	* Dynamic worker scaling, workers should survive loss of build server, pool should scale quickly
	* Spot instances for cost savings
	* Versioned testing, enable testing of infrastructure changes in topic branches based on versions
	* Improved queueing system, one centralized queue not tied to workers, let workers pull when they can
	* Less infrastructure flakinees, push testing and creation of test machines to developers, frees up dev ops team time
	* Correct privileges for better security
* ECS and Docker
	* ECS maximize usage of EC2 containers
	* Same AMI can run multiple docker images
	* IAM separation per service
* Docker
	* Update Dockerfiles and task definitions and let the CI go
	* Dockerfiles and project code live together
	* Secrets or any form of config never baked in to containers
	* Strict rules on FROM
		* Always pull from internal images they trust hosted on ECR
	* Multiple containers running on same instance, set `essential: true` in your taskDefinition so others don't continue to try to run if one fails
* Dynamic Worker Scaling
	* SQS -> SNS -> Lambda (Scaling or Bin Packing based on need, I need some clarification on this part, bin packing I think means run the jobs on the minimum number of slaves, so they can shut down machines when they are no longer needed) -> ECS

	