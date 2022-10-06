import boto3
ec2 = boto3.client('ec2', region_name='us-east-1')  
outfile = open('mykeypair.pem','w')

key_pair = ec2.create_key_pair(KeyName='mykeypair2')
MyKeyPair = key_pair["KeyMaterial"]

print(MyKeyPair)

