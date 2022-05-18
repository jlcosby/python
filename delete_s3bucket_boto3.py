#delete an s3 bucket

import boto3

#identify the aws resource as an s3 bucket - add globally unique name

s3 = boto3.client("s3")

#delete bucket

s3.delete_bucket(Bucket = "pandorasbucket22")