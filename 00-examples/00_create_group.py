import boto3

session = boto3.Session(profile_name='boto3')
iam = session.resource('iam')

group = iam.create_group(
    Path='/',
    GroupName='developer'
)

print(group)
