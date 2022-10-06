import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-026b57f3c383c2eec',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='mykeypair2'
 )

