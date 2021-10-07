import sys
import botocore
'''
try:
    import boto3
except Exception as e:
    print(e)
'''
try:
    import boto3
except ModuleNotFoundError:
    print("Boto3 in not installed. Please install boto3 and try again")    
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

try:
    aws_man_con = boto3.session.Session(profile_name = "dev")
except botocore.exceptions.ProfileNotFound:
    print('dev profile is not configured on your .aws credentials file. Use other profile or please configure dev profile.')
    sys.exit(3)
try:
    iam_con_re = aws_man_con.resource(service_name = 'iam')
    for each_user in iam_con_re.users.all():
        print(each_user)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'AccessDenied':
        print('Your profile does not have access to woek with IAM Users')
    print(e.reponse['Error']['Code'])
    sys.exit(5)
except Exception as e:
    print(e)
