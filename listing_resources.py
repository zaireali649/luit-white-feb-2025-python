from helpers import *  # Importing necessary helper functions
import json
from typing import List
import boto3


def print_bucket_names(s3_client: boto3.client) -> None:
    """
    Fetches and prints the names of all S3 buckets.

    Args:
        s3_client (boto3.client): A Boto3 S3 client instance.
    """
    bucket_names: List[str] = list_buckets(s3_client)

    # print("\n".join(bucket_names)) # Also can be done using string join
    # Print each bucket name on a new line
    for bucket_name in bucket_names:
        print(bucket_name)


def print_bucket_names_json(s3_client: boto3.client) -> None:
    """
    Fetches S3 bucket names and prints them in a JSON-formatted string.

    Args:
        s3_client (boto3.client): A Boto3 S3 client instance.
    """
    bucket_names: List[str] = list_buckets(s3_client)

    # Print bucket names as a formatted JSON string
    print(json.dumps(bucket_names, indent=4))


def print_instance_ids(ec2_client: boto3.client) -> None:
    """
    Fetches and prints the instance IDs of all EC2 instances.

    Args:
        ec2_client (boto3.client): A Boto3 EC2 client instance.
    """
    instances = describe_instances(ec2_client)
    instance_ids: List[str] = []

    # Extract instance IDs from the response
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    # Print each instance ID
    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    # Initialize AWS clients
    ec2_c = get_ec2_client()
    s3_client = get_s3_client()

    # Print S3 bucket names
    print_bucket_names(s3_client)
    
    # Print S3 bucket names in JSON format
    print_bucket_names_json(s3_client)
    
    # Print EC2 instance IDs
    print_instance_ids(ec2_c)
