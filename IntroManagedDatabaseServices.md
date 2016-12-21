Intro to Managed Database Services
==================================

#### Random Notes
* Database migration service
	* Allows taking many relational databases and migrates them to redshift, aurora, or one of the other options

#### Four Categories
* Relational
* Big Data
* No SQL/In Memory
* Analytical

#### Managed Services
* **RDS Aurora**
	* Supports MySQL, PostgreSQL, MariaDB, Oracle
	* Failing nodes are automatically replaced
	* If the primary node fails, it switches to a replica and promotes to primary in less than a minute
	* **MySQL**
		* UP to 64TB in a single with 15 read replicas
		* 500k reads/sec, 100k writes/sec
	* **PostgreSQL** also now supported

* **DyanmoDB**
	* Denormalized/hierarchical
	* Instantiated views
	* Scale horizontally
	* Emerging technology
		* Low Cost
		* Easy Administration
		* Claims 4-6 milliseconds regardless of table/collection size
		* No throughput limit/storage limit (except exabytes)
		* Very durable, deployed in 3 availability zones and always clustered
		* Consistent high performance and availability
		* Scales ondemand by itself
			* Nexon uses this and pulled 2 million users in first day, now close to 100 million and they never had to worry about scaling

* **ElastiCache**
	* Will help make all your DBs faster
	* Redis and Memcached
	* Fully managed, zero admin
	* Highly available and reliable
	* high performance in memory key value store
	* < 500 micro second latency for most commands
	* 4.5 million writes/sec and 20 million reads/sec
	* Increase speed and reduce costs of DynamoDB or RDS
	* Expedia reduced throughput from 35000 to 3500, reducing the cost 6x
* **Redshift**
	* PostgreSQL based environment, faster. simpler, cheaper
	* Massively parallel, petabyte scale
	* Fully Managed
	* HDD and SSD platforms
* **Amazon ElasticSearch Service**
	* Elastic search and Kibana
	* Centralized Logging Cloud Formation template
* **Amazon EMR**
	* MapReduce, Spark, Presto
	* Storage with S3, HDFS, or MapR
	* Leverage elasticity of cloud
	* Pay by the hour with spot instances
	
	