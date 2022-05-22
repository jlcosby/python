#terminate instances
import boto3
ec2_client=boto3.client('ec2')

#terminate a single instance
response = client.terminate_instances(
    InstanceIds=[
        'string',
    ],

#terminate multiple instances
 li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)

ec2_client.terminate_instances(InstanceIds=li)

