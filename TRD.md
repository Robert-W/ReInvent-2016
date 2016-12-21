TRD Real time Analytics
=======================

Technology used
* DynamoDB Streams
* DynamoDB
* Firehose
* Kinesis
* Lambda
* S3

#### Random Notes
* Use data and models pre-race to calculate optimal settings and adjustments for cars
* Get data to drivers for immediate feedback and help improve their lap times
* Realtime data and analytics during race scenarios
* Look into Meteor to understand how to stream data to client

#### Architecture
* Backend
	* Node.js
	* DynamoDB Streams and Mongo
	* Persistent data with DyanmoDB and S3
	* Cache - Amazon ElastiCache
* Frontend
	* Javascript with Polymer
	* Dynamic data served to clients in Meteor
	
#### Why they chose DyanmoDB
* Decoupled analysis from data collection
* Multiple sources can write to DynamoDB
* Data can be streamed out in real time
* Data is persisted permanently for future queries
* Managed service means no maintenance
* Easy access control with AWS IAM (Column, Rows, Table level)

#### DynamoDB Configurations
* Choosing the correct hash & range has enormous performance implications
	* hash
		* Determines which partition data is stored in
		* Records with equal partitions are stored on the same partition
		* To query, you must know the records hash
	* Range
		* Data with same hash is sorted in the partition by range
		* Combination of hash and range can make very fast queries
* Hot key mitigation
	* Separate tables
	* Manual partitioning
		* Add a random number to the hash
		* Results in many queries if all race data is spread across many partitions
	* Composite keys (What they use)
		* Date, type, and lap as hash
		* Data in potentially in up to 10,000 partitions
		* Can query in less than a second
		* Could further hash by car number if needed
		* Fetching data for entire race can be in parallel. If you have 10,000 partitions, which is 10,000 DynamoDB nodes, you can query them all in parallel for fast queries.
* Data Streaming
	* TRD wrote a JavaScript wrapper that does the same thing as Kinesis
	* AWS API Calls
		* ListStream
		* DescribeStream
		* GetShardIterator (Options below)
			* LATEST - Start of the race
			* TRIM_HORIZON - Resume from beginning of the race
			* AFTER/AT_SEQUENCE_NUMBER - Recover from a system crash
		* GetRecords
	* Streams only go back 24 hours, that's the max life of the stream
	
#### Sharding
* Tables have partitions and Streams have shards
* Shards are bounded by min/max hash id, min/max sequence number
* New shards created when boundaries of the current shard are exceeded, increased throughput requirements
* Problems
	* When streaming, had to monitor shard status to determine when it expired and scrape for new active iterators to stream data continuously
* Gotchas
	* Sharding is not instantaneous
* Kineses can be used to simulate streams and force re-shards
* Node.js library **Kinesalite** was used for testing

#### Turbo Mode - Firehose + Lambda
* Solves the problem of the read limits on DynamoDB streams
* Solution is to read from S3 then resume the stream
* Data from DynamoDB is read and streamed to Firehose with sequence number. (Firehose, feed it data, aggregate it, and dump in S3)
* Uses Lambda, triggered by DynamoDB Update, to leverage the AWS SDK and create a new firehose, then stream that data to an S3 Bucket
	


