# =======================================
# D. Hart wrote this
# =======================================
import boto3

aws_man_con=boto3.session.Session(profile_name="admin")
iam_con_re=aws_man_con.resource(service_name="iam",region_name="us-east-1")
ec2_con_re=aws_man_con.resource(service_name="ec2",region_name="us-east-1")
s3_con_re=aws_man_con.resource(service_name="s3",region_name="us-east-1")

"""
#List all iam users
for each_item in iam_con_re.users.all():
    print(each_item.user_name)
"""
"""
#List all ec2 instances
for each_item in s3_con_re.buckets.all():
    print(each_item.name)
"""

#List all ec2 instances
for each_item in ec2_con_re.instances.all():
    print(each_item.id)
