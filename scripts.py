# =======================================
# D. Hart wrote this
# Manual steps to see/list all IAM users:
#    Step1:  Get AWS Management Console
#    Step2:  Get IAM Console
#           Options: Users, Groups, Roles...
# =======================================
======================================
#Create multiple sessions
import boto3

aws_mag_con_root=boto3.session.Session(profile_name="root")
#aws_mag_con_ec2=boto3.session.Session(profile_name="ec2_developer")

iam_con_re=aws_mag_con_root.resource(service_name="iam", region_name="us-east-2")
iam_con_cli=aws_mag_con_root.client(service_name="iam", region_name="us-east-2")

#Listing iam users with resource object:

for each_user in iam_con_re.users.all():
    print(each_user.name)

#Listing iam users with client object

for each in iam_con_cli.list_users()['Users']:
    print(each["UserName"])
======================================
#Print IAM user names
#!/usr/bin/python3 This is for linux machines
import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)

=======================================
#Print S3 bucket names
#!/usr/bin/python3 This is for linux machines
import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
s3_con=aws_mag_con.resource('s3')

for each_buk in s3_con.buckets.all():
    print(each_buk.name)