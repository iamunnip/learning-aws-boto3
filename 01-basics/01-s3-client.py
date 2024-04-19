import boto3

client = boto3.client('s3')

client.create_bucket(
    Bucket='aki-temp-123'
)

with open('temp-file.txt', 'w') as file:
    file.write('hello world')

client.upload_file(
    Bucket='aki-temp-123',
    Filename='temp-file.txt',
    Key='temp-file.txt'
)

client.download_file(
    Bucket='aki-temp-123',
    Key='temp-file.txt',
    Filename='downloaded-temp-file.txt'
)

with open('downloaded-temp-file.txt', 'r') as file:
    print(file.read())