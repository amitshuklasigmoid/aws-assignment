# Rahul's Review
### Task 1
1. He had written a set of commands and ran it from CLI in order to complete the question,
the commands are as follows :
  - a. Providing the role with S3 full access
    ``` aws iam attach-role-policy --role-name BucketMaker --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess```
  - b. Create an IAM role with S3 full access
    ``` aws iam create-role --role-name Bucketmaker --assume-role-policy-document file://ec2-trust-policy.json```
2. To create an EC2 instance, he wrote a Python script that uses boto3 to do the job. The
code uses the Boto3 library to connect to the Amazon EC2 service and create a new
EC2 instance. It specifies the image (AMI) ID, instance type, key pair name, and tags for
instance.
3. To create an S3 bucket, he wrote a Python script that uses boto3 to do the job. The code
uses the Boto3 library to connect to the Amazon and the code creates an S3 bucket with
the name "awsassignbucket1" in the "eu-west-3" region and then lists and prints the
names of all existing buckets.
### Task 2
He had written the necessary import and initiated the required instances and created a
handler function that does the following things:
  - a. Generates a JSON object representing transaction data with various attributes.
  - b. Creates a file name for the JSON file based on the current timestamp.
  - c. Uploads the JSON data to the specified S3 bucket and file name.
  - d. Logs the creation of the S3 object using CloudWatch Logs.
  - e. Determines the number of times the Lambda function has been invoked
  - f. Stops the execution of the Lambda function after the third run.
### Task 3
He had written the necessary import and initiated the required instances and created a
handler function that does the following things:
  - a. Parses the input data from the event parameter.
  - b. Generates a timestamp using the current datetime, Adds the timestamp to the
  input data.
  - c. Converts the modified input data to a JSON string.
  - d. Uploads the JSON data to the specified S3 bucket and file name.
  - e. Prints a log message indicating the successful creation of the S3 object, Returns
       a response object with the file name and success status.
  - f. He had used Postman for sending the file using a local machine.

# Chakradhar's Review

### Task 1
1. Initially he generated access key from aws console to access aws from CLI.
2. By using AWS configure command he login into aws.
3. By using create role command role is created giving put object access.
4. Then he added s3 full access policy to it.
5. Instance profile is created using create profile command.
6. Then instance profile added to role created before.
7. By using ec2 run instance command he created an instance in the profile just created.
8. By using  s3api create-bucket command s3 bucket is created.
### Task 2
1. Initially new custom policy is created from command line.
2. By using create role command role is created with put object access.
3. Then cloud watch logs access is attached to it.
4. Lambda function is created from CLI with required parameters.
5. Then event rule is created form aws console.
6. Lambda executes for 3 time then it stops.
7. cloud watch logs are generated.

### Task 3
1. Lambda function is updated that accepts request from an API and put object in s3 bucket.
2. From ALI gateway new api is created with post request method.
3. Then he added lambda function to an API.
4. Then he tested the API and deployed it.
5. From the postman application he hit the API with json body and post request.
