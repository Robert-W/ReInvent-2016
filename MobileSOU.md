Mobile State of the Union - Serverless, New UX, Auth, & More
============================================================

#### Random Notes
* Key areas of mobile development
	* Intelligent multimodal user experiences
	* Frictionless scaling
	* User and data security
	* User engagement and analytics
* Build in decision trees with Lex very easily
* AWS Mobile Hub and Mobile SDK
	* Can generate fully functional iOS and Android code for you
	* React Native, Unity, Xamarin, iOS, Android, JavaScript
* Device Farm
	* Automated testing in parallel against a collection of physical devices in the Cloud
	* Remote Access that allows gestures, swipes, and real time interaction from the web browser
*  Mobile Hub provides GUI for adding features to your mobile application
* [AWS mobile](https://aws.amazon.com/mobile)
	
#### Intelligent multimodal user experiences
* Huge market for voice and chat bots
* Simplify complex UX flows
* Understand user intents better and personalize experiences
* Automate complex business processes
* Amazon Lex
	* Help with complex business rules for understanding many versions of the same sentence. e.g. I want pizza, I want pepperoni pizza, Give me pizza, Can I order pizza all should fire the same intent
	* Building bots for Lex is easy
	* Save development time using AWS Mobile Hub components and samples
	* Connectors in Mobile hub can invoke existing Sass applications

#### Frictionless scaling
* Serverless architecture
	* Save dev time
	* Host logic shared across platforms
	* Pay for what you use
	* High availability and low latency
	* allows you to focus on building features and minimizing operation efforts
	* Anatomy of a serverless application
		* Cognito for login
		* Invoke API's using AWS IAM
		* API Gateway -> Lambda
		* Dynamo DB (data), SNS or SES (notifications), S3 (storage)

#### User and data security
* Building a custom identity and solution is hard, especially when you need auth flows for multiple client platforms
* Cognito offers User pools and Federated identities

#### User engagement and analytics
* Amazon Mobile analytics
* Understanding user behavior is key to defining the right product experience
* Great new engagement features to be announced soon