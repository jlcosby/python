#week 15 project a

#Scenario: Our DevOps engineering team often uses a development lab to test releases of our application. The Managers are complaining about the rising cost of our development lab and need to save money by stopping our (for this example) 3 ec2 instances after all engineers are clocked out.
#Create a Python script that you can run that will stop all instances.
import boto3

#envoke ec2 client
ec2_client=boto3.client('ec2')

x=ec2_client.describe_instances()

data=x["Reservations"]
li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
ec2_client.stop_instances(InstanceIds=li)
