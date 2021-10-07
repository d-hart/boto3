# =======================================
# D. Hart wrote this
# Manual steps to see/list all IAM users:
#    Step1:  Get AWS Management Console
#    Step2:  Get IAM Console
#           Options: Users, Groups, Roles...
# =======================================
======================================
#Print IAM user names
#!/usr/bin/python3 This is for linux machines
import boto3

aws_mag_con=boto3.session.Session(profile_name="admin")
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)

=======================================
