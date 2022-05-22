#create ebs volume snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-xxxxxxxxxxxxxxxxxx',
      VolumeType='gp2')
