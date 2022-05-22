#create an EBS volume with boto3
import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1',
      Size=8,
    Encrypted=True,               
      VolumeType='gp2',
      TagSpecifications=[
          {
              'ResourceType': 'volume',
              'Tags': [
                  {
                      'Key': 'Name',
                      'Value': 'Test'
                  },
              ]
          },
      ],
     
  )
