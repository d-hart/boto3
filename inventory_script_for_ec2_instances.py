import boto3
import csv
from pprint import pprint
sts_client = boto3.client('sts')
assumed_role_object = sts_client.assume_role(
    RoleArn = ''
    RoleSessionName = ''
)