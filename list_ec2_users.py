import boto3

# aws_man_con = boto3.session.Session(profile_name='admin')
# ec2_con = aws_man_con.resource(service_name = "ec2",region_name = "us-east-1")

ec2_con = boto3.resource(service_name = "ec2",region_name = "us-east-1")

for each_instance in ec2_con.instances.all():
    print(each_instance.id,each_instance.state)