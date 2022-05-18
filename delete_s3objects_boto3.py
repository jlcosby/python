#delete s3 objects

import boto3

s3_resource=boto3.client("s3")

#delete single object

s3_resource.delete_object(Bucket='pandorasbucket22',
      Key='testimage.png')
      
#find all the objects from the bucket

objects=s3_resource.list_objects(Bucket="pandorasbucket22")["Contents"]

len(objects)

#iteration

for object in objects:
    response=s3_resource.delete_object(Bucket='pandorasbucket22',
      Key=object["Key"])
    print(response)
