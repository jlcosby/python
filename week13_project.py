#AWS Service Inventory

#Create a list of services using Python. IE: S3, Lambda, EC2, etc

#1. The list should be empty initially.
aws = []
#print(aws)

#2. Populate the list using append or insert.
aws.insert (0,'S3')
aws.insert (1,'EC2')
aws.insert (2,'CloudFront')
aws.insert (3,'CloudWatch')
aws.insert (4,'CloudFormation')

aws.append('RDS')
#print(aws)
#3. Print the list and the length of the list.
#print(aws)
#print(len(aws))

#4. Remove two specific services from the list by name or by index.
#aws.remove('RDS')

del aws[1:3]

#print(aws)
#5. Print the new list and the new length of the list.
aws = ['S3', 'CloudWatch', 'CloudFormation', 'RDS']
#print(len(aws))