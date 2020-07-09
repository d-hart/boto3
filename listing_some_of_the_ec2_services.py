# =======================================
# D. Hart wrote this
# =======================================
import boto3
from pprint import pprint

aws_man_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="us-east-1")
"""
response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response:
    for each in each_item["Instances"]:
        print("===============================")
        print("The Image Id is: {}\nThe Instance Id is: {}\nThe Instance Launch Time is: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))
"""
#Get certain information on ec2 instances
response=ec2_con_cli.describe_volumes()["Volumes"]
for each_item in response:
    pprint("The Volume Id is: {}\nThe AvailabilityZone is: {}\nThe Volume Type: {}\n".format(each_item["VolumeId"],each_item["AvailabilityZone"],each_item["VolumeType"]))

#"The Volume Id is: {}\nThe AvailabilityZone is: {}\nThe Volume Type: {}\n".format(each_item["VolumeId"],each_item["AvailabilityZone"],each_item["VolumeType"])