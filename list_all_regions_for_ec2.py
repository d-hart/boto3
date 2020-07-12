import boto3
aws_man_con=boto3.session.Session(profile_name="admin")
ec2_con_re=aws_man_con.resource(service_name="ec2")

for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
    print(each_item['RegionName'])#Search using ['RegionName'] works because you're printing multiple dictionaries