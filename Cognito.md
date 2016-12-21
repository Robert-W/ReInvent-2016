User Sign In, Management, and Security for Web Applications with Cognito
========================================================================

* Helps manage and secure your user's identity.
* Prioritize scalability upfront.
* Implementing token-based authentication.
* Support for multiple social identity providers, SAML providers.
* Can control access to AWS resources from your app.

#### Cognito user pools
* Serverless authentication and Management
* Managed User directory
* Enhanced Security features

##### Comprehensive User flows
* Sign up and Sign in
* User profile data - Users can customize their profiles including custom attributes
* Forgot password
* Token based authentication
* Email or phone number authentication
* SMS Multifactor Authentication
* Lambda Hooks
	* Custom Auth flows
		* Define auth challenge
		* Create auth challenge
		* Verify challenge responses
	* Authentication events
		* Pre and Post authentication events
	* Sign Up
		* Pre and pots sign up confirmation
	* Messaging
		* Custom messages and localization of messages
		
##### Extensive Admin capabilities
* Create and manage user pools
* Define custom attributes
* Require submission of attribute data for registration
* Set per app permissions
* Set up password policies per user pool
* Search and Manage users

#### Remembered devices
* per user allows you to build custom logic around how many devices a user can have
* suppress two-factor authentication if the token is not expired and log in is on a known device.

#### Random notes
* Importing existing users
* User pools and API Gateway can use native support or customized lambda functions.
* They have a example app using Angular 2 in their Github

#### Federated Logins with third party (steps to follow)
* Authenticate users
* Get AWS Credentials
* Access control for AWS resources

##### Lessons learned from Asurion
* Great Collaboration ??
* Recommend to build a robust testing program (and run on all changes)
* Weigh the benefits and costs of custom implementation (maintenance costs)
