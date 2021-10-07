# =======================================
# D. Hart wrote this
# =======================================
import boto3

aws_man_con_admin=boto3.session.Session(profile_name="admin")
sts_con_cli=aws_man_con_admin.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
print(response.get('UserId'))

aws_man_con_ec2_dev=boto3.session.Session(profile_name="ec2_developer")
sts_con_cli=aws_man_con_ec2_dev.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
print(response['UserId'])