#create vpc using boto3

import boto3

client=boto3.client("ec2")

client.create_vpc(CidrBlock='10.0.0.0/16')

#describe vpc

x=client.describe_vpcs


no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
#describe one vpc based on vpc id

x=client.describe_vpcs(VpcIds=["vpc-06f85a6d","vpc-0726e99e7bc27be14"])
x

#describe vpc based on filter

x=client.describe_vpcs(Filters=[
          {
              'Name': 'vpc-id',
              'Values': [
                  'vpc-06f85a6d',
                  'vpc-0726e99e7bc27be14'
                  
              ]
          },
      ])
x

#remove vpc

client.delete_vpc(
      VpcId='vpc-06f85a6d'
      
  )
  response