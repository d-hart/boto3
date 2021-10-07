
import boto3 
from botocore.exceptions import ClientError

my_session = boto3.session.Session(profile_name="faye")
client = my_session.client("ec2")
response = client.describe_instances(MaxResults=5)
print(response)
# for instance in response["Instances"]:
    # print(instance)


