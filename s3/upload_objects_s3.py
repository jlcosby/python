#upload object to s3 bucket

import boto3

#upload a single file

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="upload.png",
    Bucket="pandorasbucket22",
    Key="testimage.png")

#how to upload multiple files

import os
import glob

cwd=os.getcwd()

cwd=cwd+"/upload/"

files=glob.glob(cwd+"*.png")

files

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="pandorasbucket22",
    Key=file.split("/")[-1])
