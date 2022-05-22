#create sns pipeline
from create_sns_topic import create_sns_topic
from list_sns_topics import list_sns_topics
from add_sns_subscription import sns_subscribe_email
from publish_sns_topic import sns_publish_topic

import boto3

if __name__ == "__main__":
    sns = boto3.client('sns')
    
    topic_name = 'from_pipline'
    email = 'jennelle.cosby@gmail.com'
    message = 'You have 7 days.'
    
    create_sns_topic(sns, 'from_pipeline')
    topicArns = list_sns_topics('sns')
    topicArn = [topicArn for topicArn in topicArns if topic_name in topicArn.split(":")[-1]][0]
    
