#pip install boto3

import boto3

#create low-level service client by name using the default session

s3_resource=boto3.client('s3')

#list buckets by name

s3_resource.list_buckets()["Buckets"][0]["Name"]

#list and print buckets with formatted creation date

creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])
