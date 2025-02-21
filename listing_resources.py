from helpers import *
import json

def print_bucket_names(s3_client):
    bucket_names = list_buckets(s3_client)

    # print("\n".join(bucket_names)) # Also can be done using string join
    for bucket_name in bucket_names:
        print(bucket_name)

def print_bucket_names_json(s3_client):
    bucket_names = list_buckets(s3_client)

    print(json.dumps(bucket_names, indent=4))
   
     

def print_instance_ids(ec2_client):
    instances = describe_instances(ec2_client)
    instance_ids = []
  
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    for instance_id in instance_ids:
        print(instance_id) 


if __name__=="__main__":
    ec2_c = get_ec2_client()
    s3_client = get_s3_client()

    print_bucket_names(s3_client)
    print_bucket_names_json(s3_client)
    print_instance_ids(ec2_c)