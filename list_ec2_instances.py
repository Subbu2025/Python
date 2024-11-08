import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Specify the AWS region
region = 'us-east-1'

# Initialize a session using your credentials configured with AWS CLI
session = boto3.Session(region_name=region)

# Initialize the EC2 client
ec2_client = session.client('ec2')

# Retrieve a list of EC2 instances
def list_ec2_instances():
    try:
        print("Attempting to describe instances...")
        instances = ec2_client.describe_instances()
        if not instances['Reservations']:
            print("No instances found in the specified region.")
        else:
            print("Instances found:")
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    instance_type = instance['InstanceType']
                    state = instance['State']['Name']
                    launch_time = instance['LaunchTime']
                    print(f'Instance ID: {instance_id}')
                    print(f'Instance Type: {instance_type}')
                    print(f'State: {state}')
                    print(f'Launch Time: {launch_time}')
                    print('-' * 20)
    except NoCredentialsError:
        print("AWS credentials not found. Please configure your AWS CLI.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials found. Please check your AWS CLI configuration.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to list instances
list_ec2_instances()
