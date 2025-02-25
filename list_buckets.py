import boto3  # Import the boto3 library to interact with AWS services

s3 = boto3.client('s3')  # Create an S3 client object for interacting with Amazon S3

response = s3.list_buckets()  # Retrieve a list of all buckets from S3

buckets = response["Buckets"]  # Extract the list of buckets from the response dictionary

for bucket in buckets:  # Iterate through each bucket in the list
    print(bucket["Name"])  # Print the name of the current bucket
