import boto3
aws_man_con=boto3.session.Session(profile_name="admin")
ec2_con_re=aws_man_con.resource(service_name="ec2",region_name="us-east-1")

sts_con_cli=aws_man_con.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
my_own_id=response.get("Account")
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]:
    print(each_snap)


