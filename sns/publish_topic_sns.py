#publish to an sns topic with boto3

import boto3


#create function

def sns_publish_topic(sns_client, TopicArn, Message):
    sns_publish_topic(TopicArn=TopicArn, Message=Message)

sns = boto3.client('sns')

if __name__=="__main__":
    sns = boto3.client('sns')
    
    sns_publish_topic(sns, <topicarn>, <message>)
