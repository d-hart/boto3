# =======================================
# D. Hart wrote this
# =======================================
import boto3

aws_mag_con_root=boto3.session.Session(profile_name="admin")
#aws_mag_con_ec2=boto3.session.Session(profile_name="ec2_developer")

iam_con_re=aws_mag_con_root.resource(service_name="iam", region_name="us-east-2")
iam_con_cli=aws_mag_con_root.client(service_name="iam", region_name="us-east-2")

#Listing iam users with resource objects:

for each_user in iam_con_re.users.all():
  print(each_user.name)

print("---------------------------")
#Listing iam users with client object

for each in iam_con_cli.list_users()['Users']:
    print(each["UserName"])