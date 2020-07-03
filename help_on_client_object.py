# =======================================
# D. Hart wrote this
#
# =======================================
import boto3

aws_man_con=boto3.session.Session(profile_name="admin")
#create iam,ec2 and s3 consoles
iam_con_cli=aws_man_con.client(service_name="iam",region_name="us-east-1")
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="us-east-1")
s3_con_cli=aws_man_con.client(service_name="s3",region_name="us-east-1")
"""
#List all iam users using client object
response=iam_con_cli.list_users()
for each_item in response['Users']:
  print(each_item['UserName'])
"""
"""
#List all ec2 instances ids
response=ec2_con_cli.describe_instances()
for each_item in response['Reservations']:
  for each_instance in each_item['Instances']:
    print(each_instance['InstanceId'])
"""
#List an S3 bucket
#Great job
response=s3_con_cli.list_buckets()
for each_item in response['Buckets']:
  print(each_item['Name'])
