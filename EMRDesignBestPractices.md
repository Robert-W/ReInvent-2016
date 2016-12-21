EMR Best Practices and Design Patterns
======================================

* Look into Presto, powerful tool used by netflix to power their 25 petabyte database.
* Look at their Github as they are open sourcing many connectors
* HBASE now supports S3 as a datastore
* Access control by cluster tag and IAM roles
* Fine grained access control with apache ranger
* Encryption supported for Spark, Tez, and Map Reduce using Lux
* Auto Scaling and Spot are now available for EMR
* Coming Soon: Advanced Spot Provisioning
* Elastic Beanstalk and Elasti Cache typically sit in from to expose API's

#### YARN
* Core resource manager in EMR
* Uses capacity scheduler
	* Uses queues, can be prioritized

#### OnCluster UI's
* Hue
* Spark, Hadoop, Apahce HBASE, Tez, Flink
* You can bootstrap your own applications if you would like, such as Jupyter, RStudio

#### Storage Layers you can choose from
* Dynamo DB, RDS, ElasticSearch, Redshift, Kafka, Kinesis, or S3

#### S3 Tips
* Avoid key names in lexicographical order
* Improve throughput and S3 list performance

#### Guiding Principles for building a Data Platform
* Store all enterprise data & enable user Access
* ELT instead of ETL. Transform JIT.
* Data quality
* Data Security
* Embrace variability, velocity, and volume.
* Scale on demand without manual intervention
* Pay as you go
* Focus on value, agility, and flexible delivery




