# AWS Assignment
## Task1
### Part a
- Created an IAM role as amit with S3 Full Access 
<img width="1440" alt="Screenshot 2023-05-28 at 11 31 05 AM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/b4ceecc5-c888-4497-bf97-1b96c17700c6">

### Part b
- Created an ec2-instance as amit-ec2 with amit role that i have created in part a
<img width="1440" alt="Screenshot 2023-05-28 at 11 34 54 AM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/6093b9f4-354c-4005-a938-deceb66d2a11">

### Part c
- Configured my AWS CLI using this command<br>
   <pre>aws configure</pre>
   Then provided Access Key ID and Secret Access Key.

- Create a S3 bucket from aws CLI using this command
   <pre>aws s3api create-bucket --bucket amit1616 --region us-east-1 </pre>
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
<img width="1440" alt="Screenshot 2023-05-28 at 11 12 02 PM" src="https://github.com/amitshuklasigmoid/aws-assignment/assets/122515454/0670a713-43be-44ca-bcbe-a046e56a6da3">
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




