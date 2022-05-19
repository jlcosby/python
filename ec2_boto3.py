#starting, stopping, 
import boto3

ec2_client = boto3.client('ec2')

#create or launch an instance

ec2_resource.create_instances(ImageId='ami-xxxxxxxxxxxxxxxxxx',
      InstanceType='t2.micro',
    MaxCount=1,
      MinCount=1)
    
#create/launch multiple instances
ec2_resource.create_instances(ImageId='ami-xxxxxxxxxxxxxxxxxx',
      InstanceType='t2.micro',
    MaxCount=4,
      MinCount=3)

#describe instances 
x=ec2_client.describe_instances()

data=x["Reservations"][0]

data_instance=data["Instances"]

for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")
 
 #terminate multiple instances
 
 li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)

ec2_client.terminate_instances(InstanceIds=li)
   