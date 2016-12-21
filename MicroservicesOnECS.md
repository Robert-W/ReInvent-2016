Microservices on ECS
====================

* Small
* Decoupled
* Independent

#### Random Notes
* heard about RabbitMQ on EC2 again, might be worth checking it out. Instacart used service discovery through queues.

#### Micro services vs Monolithic Architecture
* Micro services are an evolution of SOA
* SOA typically revolves around middleware

##### Monolithic
* Everything mixed together means you have to scale the whole thing
* All developers committing code potentially into a single repository, and runs through one delivery pipeline

##### Micro services
* Decompose services into smaller individual units so they can be scaled individually
* Multiple delivery pipelines with code being checked into many various locations
* Needs some sort of service discovery
* Characteristics of a Micro Service
	* Independent
	* Decentralized
	* Black Box - When service A calls service B, they need a public interface to communicate, but dont share other things
	* Polyglot - Run different languages, versions, systems, if they are more appropriate for the use case
	* Do One thing well - Do something very specific, no side effects.
	* You build it and run it

#### Challenges of running at scale
* Resource Management
* Monitoring
	 * How do you know if a service if healthy
	 * How to you debug a service
	 * How do you check performance of a service
* Service Discovery
	* How does A know where B is
	* How does it announce itself to the world
	* Load Balancers
* Deployment
	* How do you manage all these things deploying independent of each other
	
#### ECS
* Integration with Code* services for CI/CD
* Fully ACID compliant resource and state management
* Integration with Cloud Watch for monitoring and logging
* Shared state optimistic concurrency
* Blox, may allow for custom schedulers to be used in ECS to handle tasks and services
* Schedulers
	* Batch Jobs
		* Run once
	* Long-running Apps
		* Rest endpoint for example
		* ECS service scheduler for restart
		* Scalable
		* AZ aware
		* Grouped containers - service definition can spin up multiple containers if necessary
* CD with Jenkins


