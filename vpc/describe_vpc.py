#describe vpc

x=client.describe_vpcs


no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
#describe one vpc based on vpc id

x=client.describe_vpcs(VpcIds=["vpc-xxxxxxxx","vpc-xxxxxxxxxxxxxx"])
x

#describe vpc based on filter

x=client.describe_vpcs(Filters=[
          {
              'Name': 'vpc-id',
              'Values': [
                  'vpc-xxxxxxxx',
                  'vpc-xxxxxxxxxxxxxxxx'
                  
              ]
          },
      ])
