import boto3
aws_man_con=boto3.session.Session(profile_name="admin")
ec2_con_re=aws_man_con.resource(service_name='ec2',region_name="us-east-1")
f1={"Name": "instance-state-name", "Values":["stopped"]}
f2={"Name":"instance-type","Values":["t2.micro"]}
f3={"Name":"ip-address","Values":["***.***.***.**"]}
f4={"Name":"vpc-id","Values":["vpc-*******"]}
for each in ec2_con_re.instances.filter(Filters=[f2,f1]):
    print(each)