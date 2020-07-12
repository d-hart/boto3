import boto3
aws_man_con=boto3.session.Session(profile_name="admin")
ec2_con_re=aws_man_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="us-east-1")
'''
all_instances_ids=[]
for each_in in ec2_con_re.instances.all():
    all_instances_ids.append(each_in.id)
    print(each_in.id)
#print(dir(ec2_con_re.instances))

waiter=ec2_con_cli.get_waiter("instance_running")
print("Starting all instances...")
ec2_con_re.instances.start()
waiter.wait(InstanceIds=all_instances_ids)
print("Your instance has started!")

np_sers_ids=[]
f1={"Name":"tag:Name","Values":['Non_Prod']}
for each_in in ec2_con_re.instances.filter(Filters=[f1]):
    np_sers_ids.append(each_in.id)
print(np_sers_ids)
print("-----------------------")
'''

np_sers_ids=[]
f1={"Name":"tag:Name","Values":['Non_Prod']}#Filter!
for each_item in ec2_con_cli.describe_instances(Filters=[f1])["Reservations"]:
    for each_in in each_item["Instances"]:
        np_sers_ids.append(each_in["InstanceId"])
print(np_sers_ids)

print("Starting instances with IDs of : ",np_sers_ids)
ec2_con_cli.start_instances(InstanceIds=np_sers_ids)
waiter=ec2_con_cli.get_waiter("instance_running")
waiter.wait(InstanceIds=np_sers_ids)
print("Your instances have started...")