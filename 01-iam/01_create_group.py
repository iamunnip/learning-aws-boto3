import boto3

iam = boto3.client('iam')

group = iam.create_group(
    GroupName='developer',
    Path='finance-team'
)

print(group)
