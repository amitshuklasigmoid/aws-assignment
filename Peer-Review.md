# Rahul's Review
- 1. He had written a set of commands and ran it from CLI in order to complete the question,
the commands are as follows :
  - a. Providing the role with S3 full access
    ``` aws iam attach-role-policy --role-name BucketMaker --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess```
  - b. Create an IAM role with S3 full access
    ``` aws iam create-role --role-name Bucketmaker --assume-role-policy-document file://ec2-trust-policy.json```
- 2. To create an EC2 instance, he wrote a Python script that uses boto3 to do the job. The
code uses the Boto3 library to connect to the Amazon EC2 service and create a new
EC2 instance. It specifies the image (AMI) ID, instance type, key pair name, and tags for
instance.
- 3. To create an S3 bucket, he wrote a Python script that uses boto3 to do the job. The code
uses the Boto3 library to connect to the Amazon and the code creates an S3 bucket with
the name "awsassignbucket1" in the "eu-west-3" region and then lists and prints the
names of all existing buckets.
- 4. He had written the necessary import and initiated the required instances and created a
handler function that does the following things:
  - a. Generates a JSON object representing transaction data with various attributes.
  - b. Creates a file name for the JSON file based on the current timestamp.
  - c. Uploads the JSON data to the specified S3 bucket and file name.
  - d. Logs the creation of the S3 object using CloudWatch Logs.
  - e. Determines the number of times the Lambda function has been invoked
  - f. Stops the execution of the Lambda function after the third run.
- 5. He had written the necessary import and initiated the required instances and created a
handler function that does the following things:
  - a. Parses the input data from the event parameter.
  - b. Generates a timestamp using the current datetime, Adds the timestamp to the
  input data.
  - c. Converts the modified input data to a JSON string.
  - d. Uploads the JSON data to the specified S3 bucket and file name.
  - e. Prints a log message indicating the successful creation of the S3 object, Returns
  a response object with the file name and success status.
- 6. He had used Postman for sending the file using a local machine.
