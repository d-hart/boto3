import boto3
import datetime
session = boto3.session.Session(profile_name = "admin")
iam_con_re = session.resource(service_name = 'iam')
#Get details of any iam user

''' 
iam_user_ob = iam_con_re.User('s3_developer')
#this shows all the methods available
#print(dir(iam_user_ob))
print(iam_user_ob.user_name, iam_user_ob.user_id, iam_user_ob.arn, iam_user_ob.create_date.strftime('%Y-%m-%d'))
'''
for iam_user_ob in iam_con_re.users.all():
    print(iam_user_ob)
    print(iam_user_ob.user_name, iam_user_ob.user_id, iam_user_ob.arn, iam_user_ob.create_date.strftime('%Y-%m-%d'))