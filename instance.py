# To know the current status of instances.

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['terminated']}]) # we can change this Values to 'running', etc.
    l = []

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            l.append(instance['InstanceId']) # The key value can be 'VPCid', etc..
    print(*l)
