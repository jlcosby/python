#start instances in ec2
import boto3

ec2_client = boto3.client('ec2')

#a single instance
ec2_resource.create_instances(ImageId='ami-xxxxxxxxxxxxxxxxxx',
      InstanceType='t2.micro',
    MaxCount=1,
      MinCount=1)
    
#create/launch multiple instances
ec2_resource.create_instances(ImageId='ami-xxxxxxxxxxxxxxxxxx',
      InstanceType='t2.micro',
    MaxCount=4,
      MinCount=3)
