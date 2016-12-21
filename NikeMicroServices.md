Nike - MicroServices and Macro Security Needs
=============================================

* Layer Security 
* Different communication models for different applications
* Manage secrets
* [Cerberus](http://engineering.nike.com/cerberus/)

#### Current model
Cloud, Micro services, Serverless architecture, Agile, CI/CD

#### Security
* Principle of least privilege (Give people the minimum amount of access necessary)
* Zero trust model (Validate every step of the way)
* Automation
* Self-service
* Authentication, Authorization, Encryption

#### Use Layered security
* Physical Security (Badges, etc)
* People/IAM roles - SSO to IAM Roles
* Network
	* Routing - Only expose endpoints that need to be routable
	* VPC's - Edges limit the blast radius of compromise
	* Ports/Protocols - Don't open ports/protocols that are not necessary to be open
	* Network ACL's - Control traffic in and out of the subnets
* AWS Services
* EC2 Instances

They use Cerberus, secure property store for cloud applications, to manage secrets and provide roles.
