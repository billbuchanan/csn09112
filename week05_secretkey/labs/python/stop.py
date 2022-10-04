import boto3
ec2 = boto3.client('ec2', region_name='us-east-1')  
ec2.stop_instances(InstanceIds=["i-07b0512e24xxxxxx"])

