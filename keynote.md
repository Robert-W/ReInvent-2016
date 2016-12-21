Keynote
=======

#### Instance Updates
* T2.XLarge 16GiB
* T2.2XLarge 32GiB
* R4 488 GiB, DDR4, L3Cache, 64 vCPUs
* (Q1) I3 3.3 million IOPS, 488 GiB
* (Q1) C5 atleast 2x performance over C4, Skylake processors
* Elastic GPUs for EC2
	* Can attach GPU's to any volumes, similar to how you mount EBS
	
#### Whats New
* **Amazon Lightsail**
	* VPS made easy
	* Simple Wizard to spin up EC2 instances, set up SSD, Permissions and Access management, Security Groups, DNS, and Static IP.
	* Built so you can open it up and use more AWS as you want
	* Cost is 5$ a month for base package
* **F1 instances**
	* FPGA (Field Programmable Gate Array)
	* Write your own acceleration logic
	* Has a hardware development kit
	* Toolkits for developing, packaging, and deploying to an F1 instance.
	* Previews available now, can sell your FPGA on the marketplace.
* **Amazon Athena** (Same category as EMR & Redshift)
	* Ad-hoc queries against S3, allows you to interact with data in S3 with standard SQL
	* No infrastructure required
	* pay only for queries you run
* **Amazon AI**
	* Can be voice or text powered
	* **Amazon Recognition**
		* Image Recognition service
		* Recognizes Objects, Scenes, and Faces
		* Takes an image and tells you whats in it, returns thumbnails for
		* Batch or realtime analysis
		* low cost, easy to use, always improving
	* **Amazon Polly**
		* Text to Speech
		* Takes text, spits out MP3 streams
		* The Temperature in WA is 75Deg F returns an MP3 that would say Washington and Fahrenheit
	* **Amazon LEX**
		* Natural Language Understanding & Automatic Speech Recognition
		* What is powering Alexa
		* Gets an Integrated Development Console, can trigger Lambda functions, multi-step conversations (I want pizza, what toppings, I want Pepperoni, is that all)
		* Fully managed and has enterprise connectors (Salesforce, Twilio, Facebook Manager)
* **AWS Greengrass (more for manufacturers)**
	* Local compute, messaging, and data caching
	* Secure communications
	* Built into devices at manufacture
	* Lambda functions on AWS & Devices
	* Manage from AWS Console
	* Same programming model as the cloud
* **AWS Snowball Edge**
	* Very popular to help move significant amounts of data to AWS
	* Has on board storage & compute
	* Lots of Encyption
	* 100 TB Storage
	* Clustering capabilities, allows for sharding data across multiple snowball edge's
	* S3 endpoint to async load data into S3
	* Has Amazon Greengrass and Lambda inside, equivalent of M4.4XL instance
* **AWS Snowmobile**
	* 100 Petabyte container
	* Comes in a tractor trailer

#### Updates
* Amazon Aurora now supports PostgreSQL
	* Several times faster than typical PostgreSQL databases

#### Notes
* Look into Amazon Aurora, fastest growing service at AWS.
* VMWare Cloud on AWS
	* Use existing VMWare licenses and tools
	* Seamless migration of workloads
	* Run the same software in AWS
