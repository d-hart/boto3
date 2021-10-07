import boto3
import time
aws_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")
"""
my_inst_obj=ec2_con_re.Instance("i-06fbf83b09ea88d0b")
print("Starting the instance...")
#my_inst_obj.start()
my_inst_obj.wait_until_running()#Resource waiter waits for 200sec
print("Now your instance has started.")
"""

"""
print('Starting ec2 instance...')
ec2_con_cli.start_instances(InstanceIds=[i-06fbf83b09ea88d0b])#provides InstanceIds as a list
waiter=ec2_con_cli.get_waiter("instance_running")
waiter.wait(InstanceIds=[i-06fbf83b09ea88d0b])#[] is for specific items
print("Now your ec2 instance is up and running")
"""

my_inst_obj=ec2_con_re.Instance("i-06fbf83b09ea88d0b")
print("Starting the instance...")
my_inst_obj.start()
#switch over to using the client
waiter=ec2_con_cli.get_waiter("instance_running")
waiter.wait(InstanceIds=[i-06fbf83b09ea88d0b])#40 checks after evry 15 sec
print("Now your ec2 instance is up and running")


"""
while True:
    my_inst_obj=ec2_con_re.Instance("i-06fbf83b09ea88d0b")
    print("The current status of ec2 is: ",my_inst_obj.state["Name"])
    if my_inst_obj.state["Name"]=="running":
        break
    print("Waiting to get the running status")
    time.sleep(5)
"""

#print(my_inst_obj.state)
#print("Now your instance has started.")