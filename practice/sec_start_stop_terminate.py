import boto3
import botocore


my_session = boto3.session.Session(profile_name="faye")
ec2_client = boto3.client("ec2")
response = ec2_client.start_instances()

