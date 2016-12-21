Intro to Container Management
=============================

#### Other Notes

#### AWS Continaer Ecosystem
* Foundation
* Monitoring
* CI/CD
* Security
* PaaS

#### Container Orchestration
* Service Management
	* Availability
	* Lifecycle - Upgrade/downgrade services 
	* Discovery - Checking containers into a load balancer, exposing health checks
		* Need a way to say I'm live and ready to take traffic either to public or other services in the architecture
* Scheduling
	* Placement
	* Scaling - Changing the amount of current running containers
	* Upgrades
	* Rollback
* Resource Management
	* Memory
	* Ports
	* CPU

#### Schedulers
* Monolithic
	* Controls all resources
	* Ones run job at a time
* Two-level
	* Pessimistic locking - ensures resources are not taken before a job confirms those are needed
* Shared State
	* Optimistic concurrency
	
#### CoreOS Tectonic (Kubernetes)
* Platform for running Microservices
* Pros - Excels at application lifecycle management
* Con - Kubernetes is not easy to get started with and manage, need someone with experience
* [Tectonic](https://tectonic.com) extends Upstream Kubernetes
	* Installer
	* GUI Management console
	* Cluster scaling
	* Role based authentication
	* Comes packaged with CoreOS, tested against Docker and rkt
	* Rolling upgrades of OS
	* Disaster Recovery
	* [github.com/coreos/kube-aws](https://github.com/coreos/kube-aws)
	* Much more...
	
#### Docker Datacenter (DDC)
* Commercially supported software built around Docker engine
* Universal Control Plane
	* Cluster manager
	* Etcd for state management
	* LDAP integration
	* UCP Manager has nice GUI to manage your cluster
	* Swarm Mode
	* Image signing and runtime enforcement
	* Can push local logs to CloudWatch
* Docker Trusted Registry
	* S3 Backend support	
	* LDAP support
* DDC Quickstart with AWS architecture
* Useful if your development workflow is built around docker-compose

#### Mesosphere DC/OS (Mesos + Marathon)
* Zookeeper is the background framework.
* Can survive failure of the master node with very little disruption
* Admin Ruoter, open source ngingx authentication
* Comes with Minuteman load balancer

#### Amazon ECS
* Manage containers at scale on AWS
* ECS is a managed service
* Has the following components
	* Task
	* Task Definition
	* Cluster
	* Manager
	* Scheduler
	* Agent
* Use if you want a managed service that scales with you, leverage native integrations, build around aws tools