import boto3

s3 = boto3.resource('s3')

bucket = s3.create_bucket(
    Bucket='aki-temp-123'
)

list(s3.buckets.all())
    
bucket = s3.Bucket(name='aki-temp-123')

with open('temp-file.txt', 'w') as file:
    file.write('hello world')

bucket.upload_file(
    Filename='temp-file.txt',
    Key='temp-file.txt'
)

bucket.download_file(
    Key='temp-file.txt',
    Filename='downloaded-temp-file.txt'
)

with open('downloaded-temp-file.txt', 'r') as file:
    print(file.read())