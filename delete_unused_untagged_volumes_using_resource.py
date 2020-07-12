import boto3
aws_man_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_man_con.resource(service_name="ec2",region_name="us-east-1")
#Put resources into variables, then use attribute on them
f_ebs_unused={"Name":"status","Values":["available"]}#Fliter syntax
for each_volume in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):
    if not each_volume.tags:
        print(each_volume.id,each_volume.state,each_volume.tags)

