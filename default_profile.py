# =======================================
# D. Hart wrote this
# Using the Default session
#    Step1: Delete .aws directory(Config and Credentials)
#    Step2: Run aws configure
#    Step3: Enter access key id and secret access key
# =======================================
#Default Session
import boto3
#aws_mag_con=boto3.session.Session(profile="root")
#iam_con=aws_mag_con.resource("iam")

iam_con=boto3.resource(service_name="iam",region="us-east-2")

for each_user in iam_con.users.all():
    print(each_user.name)
# =======================================
#Custom Session

import boto3

aws_mag_con=boto3.session.Session(profile="admin")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region="us-east-1")