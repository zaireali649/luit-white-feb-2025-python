"""Script for creating AWS EC2 instances."""
from helpers import *  # Import necessary helper functions
import boto3  # Ensure boto3 is imported for typing


def create_instances(ec2_client: boto3.client, ami_type: str = "ubuntu", num_instances: int = 1) -> None:
    """Create EC2 instances based on the specified AMI type.

    Args:
        ec2_client (boto3.client): The EC2 client used for instance creation.
        ami_type (str, optional): The type of AMI to use (default is "ubuntu").
                                  Supported values: "ubuntu", "linux2023", "linux2".
        num_instances (int, optional): The number of instances to create (default is 1).

    Returns:
        None
    """
    for i in range(num_instances):
        ami_normalized = ami_type.lower().replace(" ", "")  # Normalize input to remove case sensitivity and spaces

        if ami_normalized == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Call function to create an Ubuntu instance
            print("Created Ubuntu")
        elif ami_normalized == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)  # Call function to create an Amazon Linux 2023 instance
            print("Created Linux 2023")
        elif ami_normalized == "linux2":
            create_amazon_linux_2_instance(ec2_client)  # Call function to create an Amazon Linux 2 instance
            print("Created Linux 2")
        else:
            print(f"AMI '{ami_type}' Not Supported")  # Handle unsupported AMI types


if __name__ == "__main__":
    ec2_client = get_ec2_client()  # Get EC2 client instance

    # Test cases to create different EC2 instances
    create_instances(ec2_client)  # Default to Ubuntu
    create_instances(ec2_client, "linux2023")  # Linux 2023
    create_instances(ec2_client, " LiNux  2 ")  # Linux 2 (with extra spaces and mixed case)
    create_instances(ec2_client, num_instances=2)  # Two Ubuntu instances
    create_instances(ec2_client, "linux2023", num_instances=4)  # Four Linux 2023 instances
    create_instances(ec2_client, "Windows", num_instances=5)  # Unsupported AMI type
