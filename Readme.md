# AWS Assignment
## Task1
- Configure you AWS CLI.<br>
   <pre>aws configure</pre>
    Then provide Access Key ID, Secret Access Key, Default region name.

- Create a file policy.json and add the AssumeRolePolicyDocument.<br>
	<pre>{
		"Version": "2012-10-17",
		"Statement": {
			"Effect": "Allow",
				"Principal": {
					"Service": “s3.amazonaws.com”
					“AWS” : “arn:aws:iam::0039*****9674:user/amit”
					},
			"Action": "sts:AssumeRole"
			}
		}

- Create an IAM role 
    <pre>aws iam create-role --role-name amit --assume-role-policy-document file://policy.json</pre>

- Add permission to the role 
    <pre>aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --role-name amit

- Use this role 
    <pre>aws sts assume-role --role-arn arn:aws:iam::0039*****9674:role/amit --role-session-name my-session --duration-seconds 3600<\pre>

- Make a profile that uses these credentials
   <pre>  aws configure —profile amit set aws_access_key_id access_key_id
	 aws configure --profile amit set aws_secret_access_key secret_access_key
	 aws configure --profile amit set aws_session_token session_token


<img width="789" alt="Screenshot 2023-05-17 at 6 56 37 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/2e8332ce-09e2-45c7-9338-00128fb1990d">

- create an EC2 instance with above role
    <pre>aws ec2 run-instances --image-id ami-0889a44b331db0194 --instance-type t2.micro --key-name amit --subnet-id subnet-0e5645c5c4574a239 --security-group-ids sg-0f986340ba1b0aaeb --region us-east-1 --profile amit<br>

<img width="1440" alt="Screenshot 2023-05-17 at 12 57 25 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/029bbe64-c8af-4602-bee6-43671689997b">

- create aws bucket from aws CLI
<img width="812" alt="Screenshot 2023-05-17 at 1 00 45 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/619e3663-ca72-44e0-9ace-c7233f69da17">


## Task2
- Create role for aws lambda which have put object access
- Add role to generate and access Cloudwatch logs Creating cloudwatch policy

<img width="1440" alt="Screenshot 2023-05-17 at 1 01 46 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/4f7c5f2f-5efe-4aa6-82e3-c1f74cf77aa1">
<img width="1440" alt="Screenshot 2023-05-17 at 1 13 06 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/3349efa2-19d7-4c9c-9f81-5225120ec580">

- Create a lambda_handler function to save the file in json in format and upload it to the bucket
Schedule the job to run every minute. Stop execution after 3 runs
Using amazon lambda, created a function and uploaded the file created above
<img width="1440" alt="Screenshot 2023-05-17 at 1 04 10 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/818e6e2f-d974-4d11-88af-86e493424eed">
<img width="1440" alt="Screenshot 2023-05-17 at 1 07 20 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/f85978e8-d55c-4ccb-9245-d903bd291268">
<img width="1440" alt="Screenshot 2023-05-17 at 1 13 23 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/57f960fd-e719-4667-8248-25aa48ecfe4a">
<img width="1440" alt="Screenshot 2023-05-17 at 1 13 25 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/5553b9a3-c8f3-4ee2-818f-c01ead7196aa">
<img width="1440" alt="Screenshot 2023-05-17 at 1 16 14 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/1c40b665-f1b2-4ff3-962a-ab28a5853542">
<img width="1440" alt="Screenshot 2023-05-17 at 1 16 30 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/6ff83b73-4152-4382-be8e-545ac92ff0d5">
<img width="1440" alt="Screenshot 2023-05-17 at 1 16 33 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/32dbe364-e641-4137-8d9c-87c1ceddb8cb">
<img width="1440" alt="Screenshot 2023-05-17 at 1 17 52 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/da4e9a8a-5cc4-4406-9a57-2e9d97f1ec0d">
<img width="1440" alt="Screenshot 2023-05-17 at 1 18 09 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/4e79a6c0-2628-40ce-83ec-938c6a37fca1">
<img width="747" alt="Screenshot 2023-05-17 at 10 50 25 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/bf4b2e01-6b19-4601-baff-463c4e44cc5f">


## Task 3
- a. Modify lambda function to accept parameters and return file name Modified lambda function is :
- b. Create a POST API from API Gateway, pass parameters as request body to Lambda job. Return filename and status code as response.
- c. Consume API from local machine and pass unique data to lambda.
- d. Check if cloud watch logs are generated
To create a post API to feed to lambda job these steps were followed 

```
Go to the API Gateway console and click "Create API".
Select "REST API" and click "Build".
Choose "New API" and enter a name for your API. Click "Create API".
Click "Create Resource" to create a new resource under your API.
Enter a name for your resource and click "Create Resource".
Click "Create Method" and select "POST" from the dropdown.
Select "Lambda Function" and check the "Use Lambda Proxy integration" box.
Enter the name of your Lambda function in the "Lambda Function" field and click "Save".
Deploy your API by clicking "Actions" > "Deploy API". Select "New Stage" and enter a name for your stage. Click "Deploy".
Note the URL of your API endpoint

```

<img width="1440" alt="Screenshot 2023-05-17 at 1 23 44 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/d76249b6-4007-4195-bac8-6d1a764bde25">
<img width="1440" alt="Screenshot 2023-05-17 at 1 25 41 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/9a2a9e7d-9753-416c-a771-db1eaed76906">

<img width="1440" alt="Screenshot 2023-05-17 at 1 25 57 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/ee12adaf-7c21-45fc-92c9-d0f915568fbc">
<img width="1440" alt="Screenshot 2023-05-17 at 1 26 06 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/6d3dcec2-0618-4afb-b538-b6c107ccb390">

<img width="1440" alt="Screenshot 2023-05-17 at 1 27 13 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/9e1ad0b1-2c23-4e94-a473-cb58823617f0">
<img width="1440" alt="Screenshot 2023-05-17 at 1 27 36 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/05a36d1c-c19d-4006-aee2-917b65eb0048">
<img width="1440" alt="Screenshot 2023-05-17 at 2 07 29 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/1c49b4b1-16a5-4fa0-9f6f-ebbbd6c1069e">

<img width="1440" alt="Screenshot 2023-05-17 at 2 08 04 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/027bd66e-91dd-4be3-938f-9019cafa6883">
<img width="1440" alt="Screenshot 2023-05-17 at 2 08 19 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/f19dea79-e679-4243-91f8-2507a44791e8">




