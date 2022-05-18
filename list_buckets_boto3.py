#list s3 buckets

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

#access the dictionary "Buckets" with the name bucket

buckets = response['Buckets']

#list all buckets using key "Name"

for bucket in buckets:
    print(bucket["Name"])