import boto3
from random import choice

def get_iam_client_object():
    session = boto3.session.Session(profile_name = "dev_root")
    iam_client = session.client(service_name = 'iam', region_name = 'us-east-1')
    return iam_client

def get_random_password():
    len_of_password = 8
    valid_chars_for_passwords = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    random_pass =''.join(choice(valid_chars_for_passwords) for each_char in range(len_of_password))
    return random_pass

def main():
    iam_client = get_iam_client_object()
    iam_user_name = 'doitwithpython@example.com'
    password = get_random_password()
    policy_arn = ''
    try:
        iam.client.create_user(UserName = iam_user_name)
    except Exception as e:
        if e.reponse['Error']['Code']=='EntityAlreadyExists':
            print('Already iam User with {} exists.'.format(iam_user_name))
            sys.exit.(0)
        else:
            print 'Please verify the following error and retry'
            print e
    iam.client.create_login_profile(UserName = iam_user_name, Password = password, PasswordResetRequired = False)
    iam.client.attach_user_policy(Username = iam_user_name, PolicyArn = policy_arn)
    print 'Iam User Name = {} and Password = {}'.format(iam_user_name,password)

if __name__ =="__main__":
    main()

