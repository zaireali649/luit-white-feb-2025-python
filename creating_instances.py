from helpers import * 

def create_instances(ec2_client, ami_type="ubuntu", num_instances=1):
    for i in range(num_instances):
        if ami_type.lower().replace(" ", "") == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")
        elif ami_type.lower().replace(" ", "") == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")
        elif ami_type.lower().replace(" ", "") == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")
        else:
            print("AMI Not Supported")

if __name__=="__main__":
    ec2_client = get_ec2_client()
    create_instances(ec2_client)
    create_instances(ec2_client,  "linux2023")
    create_instances(ec2_client,  " LiNux  2 ")
    create_instances(ec2_client, num_instances=2)
    create_instances(ec2_client,  "linux2023", num_instances=4)
    create_instances(ec2_client,  "Windows", num_instances=5)
