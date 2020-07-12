import boto3

aws_man_con=boto3.session.Session(profile_name="ec2_developer")
"""
ec2_con_re=aws_man_con.resource(service_name="ec2",region_name="us-east-1")
#Put resources into variables, then use attribute on them
f_ebs_unused={"Name":"status","Values":["available"]}#Fliter syntax
for each_volume in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):
    if not each_volume.tags:
        print(each_volume.id,each_volume.state,each_volume.tags)
        print("Deleting usused and untagged volumes...")
        each_volume.delete()

print("Deleted all unused and untagged volumes.")
"""
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="us-east-1")
for each_volume in ec2_con_cli.describe_volumes()["Volumes"]:
    if not "Tags" in each_volume and each_volume["State"]=="available":#if there are no tags and volume is unused, display the item
        print(each_volume["VolumeId"])
        print("===================")
#ec2_volume_filter={"Name":"","Value":[""]}
#ec2_con_cli.describe_volumes.(Filters)