# =======================================
# D. Hart wrote this
# =======================================
import boto3
from pprint import pprint

aws_man_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="us-east-1")
response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response: 
    pprint(each_item['Instances'])