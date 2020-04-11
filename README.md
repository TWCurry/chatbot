Meta-Chatbot
=======
A simple test serverless chatbot project, that I'm coding while stuck in lockdown over easter 😊 <br>
The chatbot is hosted on AWS, running on some Lambda functions and using API Gateway for the API. 

## Architecture
The system is built using the AWS Serverless Application Model (SAM), and uses a series of Lambda functions for the backend processing. For the database backend, AWS DynamoDB is used. Everything is deployed using Cloudformation through the SAM Template (template.yaml).

### Functions
#### 