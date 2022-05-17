#creating an s3 bucket using boto3

#pip install boto3
import boto3

#identify the aws resource as an s3 bucket - add globally unique name
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("pandorasbucket22")

#create the bucket - public read access. Default region is us-east-1
response = bucket.create(
    ACL = 'public-read'
    
    
)

print(response)