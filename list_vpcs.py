import boto3  # Import the boto3 library to interact with AWS services

vpc_client = boto3.client('ec2')  # Create an EC2 client to interact with Amazon EC2

response = vpc_client.describe_vpcs()  # Retrieve information about all VPCs

vpcs = response['Vpcs']  # Extract the list of VPCs from the response dictionary

for vpc in vpcs:  # Iterate over each VPC in the list
    print(vpc['VpcId'])  # Print the unique identifier of the current VPC
