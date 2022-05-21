#add sns subscription with boto3

import boto3


#create function

def sns_subscribe_email(sns_client, TopicArn, email_address):
    sns_client.subscribe(TopicArn=TopicArn, Protocol='email', Endpoint=email_address)
    
if __name__=="__main__":
    sns = boto3.client('sns')
    
    sns_subscribe_email(sns, <topicarn>, <emailaddress>)