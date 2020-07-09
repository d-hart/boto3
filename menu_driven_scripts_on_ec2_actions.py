import boto3
import sys
aws_man_con=boto3.session.Session(profile_name="admin")
ec2_con_re=aws_man_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="us-east-1")

while True:
    print("This script performs the following actions on ec2 instances")
    print("""
        1.Start
        2.Stop
        3.Terminate
        4.Exit
        """)
    opt=int(input("Enter your option: "))
    if opt==1:
        instance_id=input("Enter your EC2 Instance Id:")#use i-06fbf83b09ea88d0b
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        my_req_instance_object.start()
        print("Starting ec2 instance....")
    elif opt==2:
        instance_id=input("Enter your EC2 Instance Id:")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        my_req_instance_object.stop()
        print("Stopping ec2 instance....")
    elif opt==3:
        instance_id=input("Enter your EC2 Instance Id:")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        my_req_instance_object.Terminate()
        print("Terminate ec2 instance....")
    elif opt==4:
        print("Thank you for using this script")
        sys.exit()
    else:
        print("Your input is invalid, please try again...")