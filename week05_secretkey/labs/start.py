import boto3
ec2 = boto3.client('ec2', region_name='us-east-1')  
ec2.start_instances(InstanceIds=["i-07b0512e24xxxxxx"])

