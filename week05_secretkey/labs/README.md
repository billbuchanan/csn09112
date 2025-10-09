
![](https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png)

# Lab 4: Symmetric Key and Hashing

Part 1 Demo: [here](http://youtu.be/HbVenKMGRmE)

We will use OpenSSL for a few tutorial examples. If you want to find out more about the program, discover [here](https://asecuritysite.com/openssl/). Log into vSoC 2, and select your Kali host on the public network. You should open up the lab in your Kali instance so that you can copy and paste from the document into your Kali console. The link is here:

https://github.com/billbuchanan/csn09112/tree/master/week05_secretkey/labs 

![](https://github.com/billbuchanan/csn09112/blob/master/zadditional/kali001.png)

## A Symmetric Key

| No | Description | Result | 
|-------|--------|---------|
| 1 | Log into vSoC 2, and select your Kali host on the public network. | What is your IP address? |
| 2 | Use: ```openssl list -cipher-commands``` | Outline five encryption methods that are supported:   |
| 3 | Use: ```openssl version``` | Outline the version of OpenSSL:    |
| 4 | Using openssl and the command in the form: ```openssl prime -hex 1111``` | Check if the following are prime numbers: |  42 [Yes][No] 1421 [Yes][No] | 
| 5 | Now create a file named myfile.txt (either use nano or another editor). Next. encrypt with aes-256-cbc <br> ```openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin -pbkdf2``` and enter your password. | Use the following command to view the output file: ```cat encrypted.bin``` Is it easy to write out or transmit the output: [Yes][No]. What does the ```-pbkdf2``` part do? | 
| 6 | Now repeat the previous command and add the –base64 option. <br>```openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin –base64 -pbkdf2``` | Use the following command to view the output file: ```cat encrypted.bin``` Is it easy to write out or transmit the output: [Yes][No]
| 7 | Now repeat the previous command and observe the encrypted output. <br>```openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin –base64 -pbkdf2``` | Has the output changed? [Yes][No] Why has it changed? |
| 8 | Now let’s decrypt the encrypted file with the correct format: ```openssl enc -d -aes-256-cbc -in encrypted.bin -pass pass:napier -base64 -pbkdf2``` Has the output been decrypted correctly? | What happens when you use the wrong password? |
| 9 | If you are working in the lab, now give your secret passphrase to your neighbour, and get them to encrypt a secret message for you.  To receive a file, you listen on a given port (such as Port 1234) ```nc -l -p 1234 > enc.bin``` And then send to a given IP address with: ```nc -w 3 [IP] 1234 < enc.bin``` | Did you manage to decrypt their message? [Yes][No] | 


10.  With OpenSSL, we can define a fixed salt value that has been used in the cipher process. For example, in Linux:

```
echo -n "Hello" | openssl enc -aes-128-cbc -pass pass:"london" -e -base64 -S 241fa86763b85341 -pbkdf2
```
and then decrypt:
```
echo 9Z+NtmCdQSpmRl+eZebFXQ== | openssl enc -aes-128-cbc -pass pass:"london" -d  -base64 -S 241fa86763b85341 -pbkdf2

Hello     
```  

For a ciphertext for 256-bit AES CBC and a message of “Hello” with a salt value of  ```241fa86763b85341```, try the following passwords, and determine the password used for a ciphertext of ```tZCdiQE4L6QT+Dff82F5bw==```   [qwerty][inkwell][london][paris][cake]


11. Now, use the decryption method to prove that you can decrypt the ciphertext.

```
echo tZCdiQE4L6QT+Dff82F5bw== | openssl enc -aes-256-cbc -pass pass:"password" -d  -base64 -S 241fa86763b85341 -pbkdf2
```

Did you confirm the right password? [Yes/No] 

12.  Investigate the following commands by running them several times:
```
echo -n "Hello" | openssl enc -aes-128-cbc -pass pass:"london" -e -base64 -S 241fa86763b85341 -pbkdf2
echo -n "Hello" | openssl enc -aes-128-cbc -pass pass:"london" -e -base64 -salt -pbkdf2
```
What do you observe? Why do you think causes the changes? 

13. We don't always need to use a file to save the cipher, too. With the following, we will encrypt the plaintext of "melon":

```
echo "melon" | openssl enc -e -aes-128-cbc  -pass pass:stirling -base64 -pbkdf2         
U2FsdGVkX18cryB3vdNj+Tax1PGecO6ZOW2WL1LmdKQ=
```
and then we can decrypt with:

```
echo "U2FsdGVkX18cryB3vdNj+Tax1PGecO6ZOW2WL1LmdKQ=" | openssl enc -d -aes-128-cbc -pass pass:stirling -base64 -pbkdf2

melon
```

Now crack the following cipher using a Scottish city as a password (the password is in lower case):

```
U2FsdGVkX1+7VpBGwevibQGgescaz5nsArtGLNqFaXk=
```

What is the fruit in the plaintext?

Now try:

```
U2FsdGVkX18vpjgccu7VkPZrkncqADuy1kVKU9LbLec=
```

What is the fruit?

## B Hashing
Video: [here](http://youtu.be/Xvbk2nSzEPk)

The current Hashcat version on Kali has problems with a lack of memory. To overcome this, install Hashcat 6.0.0. On Kali on your public network, first download Hashcat 6.0.0:

```
wget https://hashcat.net/files/hashcat-6.0.0.7z
```

Next, unzip it into your home folder:

```
p7zip -d hashcat-6.0.0.7z
```

Then from your home folder, setup a link to Hashcat 6.0.0:

```
# ln -s hashcat-6.0.0/hashcat.bin  hashcat
```
and then run Hashcat put “./” in from of the program name, such as:
```
# ./hashcat –version
v6.0.0
```


### Q1 
Using: [here](http://asecuritysite.com/encryption/md5) Match the hash signatures with their words (“Falkirk”, “Edinburgh”, “Glasgow” and “Stirling”). 
```
03CF54D8CE19777B12732B8C50B3B66F  
```
Is it [Falkirk][Edinburgh][Glasgow][Stirling]? 

```
D586293D554981ED611AB7B01316D2D5 
```
Is it [Falkirk][Edinburgh][Glasgow][Stirling]? 
```
48E935332AADEC763F2C82CDB4601A25 
```
Is it [Falkirk][Edinburgh][Glasgow][Stirling]? 
```
EE19033300A54DF2FA41DB9881B4B723 | D5862: 
```
Is it [Falkirk][Edinburgh][Glasgow][Stirling]? 


### Q2
Using: [here](http://asecuritysite.com/encryption/md5) Determine the number of hex characters in the following hash signatures. 

MD5 hex chars: 

SHA-1 hex chars:

SHA-256 hex chars: 

How does the number of hex characters relate to the length of the hash signature: |

### Q3
On Kali, for the following /etc/shadow file, determine the matching password (the passwords are password, napier, inkwell and Ankle123):

```
bill:$apr1$waZS/8Tm$jDZmiZBct/c2hysERcZ3m1 
```
Bill’s password: 
```
mike:$apr1$mKfrJquI$Kx0CL9krmqhCu0SHKqp5Q0 
```
Mike’s password: 
```
fred:$apr1$Jbe/hCIb$/k3A4kjpJyC06BUUaPRKs0 
```
Fred’s password: 
```
ian:$apr1$0GyPhsLi$jTTzW0HNS4Cl5ZEoyFLjB. 
```
Ian’s password: 
```
jane: $1$rqOIRBBN$R2pOQH9egTTVN1Nlst2U7. 
```
Jane’s password: 

[Hint: openssl passwd -apr1 -salt ZaZS/8TF napier] 


### Q4
On Kali, download the following: [here](http://asecuritysite.com/files02.zip) and the files should have the following MD5 hashes : 

```
MD5(1.txt)= 5d41402abc4b2a76b9719d911017c592 
MD5(2.txt)= 69faab6268350295550de7d587bc323d 
MD5(3.txt)= fea0f1f6fede90bd0a925b4194deac11 
MD5(4.txt)= d89b56f81cd7b82856231e662429bcf2 
```

Which file(s) have been modified: 

Note: Use can use md5sum to compute MD5 hashes.

### Q5
From Kali, download the following ZIP file: [here](http://asecuritysite.com/letters.zip )

View the letters. Are they different? Now determine the MD5 signature for them. What can you observe from the result? 


## C Hashing Cracking (MD5)
Video: [here](http://youtu.be/Xvbk2nSzEPk)


### Q1
On Kali, next create a word file (words) with the words of “napier”, “password” “Ankle123” and “inkwell”

Using hashcat crack the following MD5 signatures (hash1):
```
232DD5D7274E0D662F36C575A3BD634C
5F4DCC3B5AA765D61D8327DEB882CF99
6D5875265D1979BDAD1C8A8F383C5FF5
04013F78ACCFEC9B673005FC6F20698D
```
Command used:
```
hashcat –m 0 hash1 words
```
232DD...634C Is it [napier][password][Ankle123][inkwell]?

5F4DC...CF99 Is it [napier][password][Ankle123][inkwell]?

6D587...5FF5 Is it [napier][password][Ankle123][inkwell]?

04013...698D Is it [napier][password][Ankle123][inkwell]?


Note: use the --show option to show the results of the cracking.

### Q3
Using the method used in the first part of this tutorial, find crack the following for names of fruits such as "orange", "apple", "banana", "pear", "peach" (the fruits are all in lowercase):

```
FE01D67A002DFA0F3AC084298142ECCD
1F3870BE274F6C49B3E31A0C6728957F
72B302BF297A228A75730123EFEF7C41
8893DC16B1B2534BAB7B03727145A2BB
889560D93572D538078CE1578567B91A
```

FE01D:

1F387:

72B30:

8893D:

88956:

## Hashing Cracking (LM Hash/Windows)
All of the passwords in this section are in lowercase. http://youtu.be/Xvbk2nSzEPk


### Q1
On Kali, and using John the Ripper, and using a word list with the names of fruits, crack the following pwdump passwords:
```
fred:500:E79E56A8E5C6F8FEAAD3B435B51404EE:5EBE7DFA074DA8EE8AEF1FAA2BBDE876:::
```
Fred's password: 
```
bert:501:10EAF413723CBB15AAD3B435B51404EE:CA8E025E9893E8CE3D2CBF847FC56814:::
```
Bert's password:

### Q2
On Kali, and using John the Ripper, the following pwdump passwords (they are names of major Scottish cities/towns):

```
Admin:500:629E2BA1C0338CE0AAD3B435B51404EE:9408CB400B20ABA3DFEC054D2B6EE5A1:::
fred:501:33E58ABB4D723E5EE72C57EF50F76A05:4DFC4E7AA65D71FD4E06D061871C05F2:::
bert:502:BC2B6A869601E4D9AAD3B435B51404EE:2D8947D98F0B09A88DC9FCD6E546A711:::
```

Admin:

Fred:

Bert:

### Q3
On Kali, and using John the Ripper, crack the following pwdump passwords (they are the names of animals):
```
fred:500:5A8BB08EFF0D416AAAD3B435B51404EE:85A2ED1CA59D0479B1E3406972AB1928:::
bert:501:C6E4266FEBEBD6A8AAD3B435B51404EE:0B9957E8BED733E0350C703AC1CDA822:::
admin:502:333CB006680FAF0A417EAF50CFAC29C3:D2EDBC29463C40E76297119421D2A707:::
```

Fred:

Bert:

Admin:

Repeat all 7.1, 7.2 and 7.3 using Ophcrack, and the rainbow table contained on the instance (rainbow_tables_xp_free).

## D AWS Cryptography
We are generally moving our security into the public cloud, and thus many of our keys are stored there. In AWS, we use KMS (Key Management System), and can create either symmetric keys or asymmetric keys (public keys).

### Symmetric key

With symmetric key encryption, Bob and Alice use the same encryption key to encrypt and decrypt:

![image](https://asecuritysite.com/public/kms_30.png)

Normally we use AES encryption for this. Initially, in KMS, we create a new key within our Customer managed keys:

![image](https://asecuritysite.com/public/kms01.png)

and then create the key:

![image](https://asecuritysite.com/public/kms02.png)

Next, we give it a name:

![image](https://asecuritysite.com/public/kms03.png)

And then define the adminstrative permission (those who can delete it):

![image](https://asecuritysite.com/public/kms04.png)


And the usage:


![image](https://asecuritysite.com/public/kms05.png)



The policy is then:
```
{
    "Id": "key-consolepolicy-3",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::22222222:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow access for Key Administrators",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::22222222:role/LabRole",
                    "arn:aws:iam::22222222:role/aws-service-role/trustedadvisor.amazonaws.com/AWSServiceRoleForTrustedAdvisor",
                    "arn:aws:iam::22222222:role/aws-service-role/events.amazonaws.com/AWSServiceRoleForCloudWatchEvents",
                    "arn:aws:iam::22222222:role/EMR_EC2_DefaultRole",
                    "arn:aws:iam::22222222:role/aws-service-role/elasticache.amazonaws.com/AWSServiceRoleForElastiCache",
                    "arn:aws:iam::22222222:role/aws-service-role/organizations.amazonaws.com/AWSServiceRoleForOrganizations",
                    "arn:aws:iam::22222222:role/EMR_DefaultRole",
                    "arn:aws:iam::22222222:role/EMR_AutoScaling_DefaultRole",
                    "arn:aws:iam::22222222:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9",
                    "arn:aws:iam::22222222:role/aws-service-role/support.amazonaws.com/AWSServiceRoleForSupport"
                ]
            },
            "Action": [
                "kms:Create*",
                "kms:Describe*",
                "kms:Enable*",
                "kms:List*",
                "kms:Put*",
                "kms:Update*",
                "kms:Revoke*",
                "kms:Disable*",
                "kms:Get*",
                "kms:Delete*",
                "kms:TagResource",
                "kms:UntagResource",
                "kms:ScheduleKeyDeletion",
                "kms:CancelKeyDeletion"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::22222222:role/LabRole",
                    "arn:aws:iam::22222222:role/aws-service-role/trustedadvisor.amazonaws.com/AWSServiceRoleForTrustedAdvisor",
                    "arn:aws:iam::22222222:role/aws-service-role/events.amazonaws.com/AWSServiceRoleForCloudWatchEvents",
                    "arn:aws:iam::22222222:role/EMR_EC2_DefaultRole",
                    "arn:aws:iam::22222222:role/aws-service-role/elasticache.amazonaws.com/AWSServiceRoleForElastiCache",
                    "arn:aws:iam::22222222:role/aws-service-role/organizations.amazonaws.com/AWSServiceRoleForOrganizations",
                    "arn:aws:iam::22222222:role/EMR_DefaultRole",
                    "arn:aws:iam::22222222:role/EMR_AutoScaling_DefaultRole",
                    "arn:aws:iam::22222222:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9",
                    "arn:aws:iam::22222222:role/aws-service-role/support.amazonaws.com/AWSServiceRoleForSupport"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow attachment of persistent resources",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::22222222:role/LabRole",
                    "arn:aws:iam::22222222:role/aws-service-role/trustedadvisor.amazonaws.com/AWSServiceRoleForTrustedAdvisor",
                    "arn:aws:iam::22222222:role/aws-service-role/events.amazonaws.com/AWSServiceRoleForCloudWatchEvents",
                    "arn:aws:iam::22222222:role/EMR_EC2_DefaultRole",
                    "arn:aws:iam::22222222:role/aws-service-role/elasticache.amazonaws.com/AWSServiceRoleForElastiCache",
                    "arn:aws:iam::22222222:role/aws-service-role/organizations.amazonaws.com/AWSServiceRoleForOrganizations",
                    "arn:aws:iam::22222222:role/EMR_DefaultRole",
                    "arn:aws:iam::22222222:role/EMR_AutoScaling_DefaultRole",
                    "arn:aws:iam::22222222:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9",
                    "arn:aws:iam::22222222:role/aws-service-role/support.amazonaws.com/AWSServiceRoleForSupport"
                ]
            },
            "Action": [
                "kms:CreateGrant",
                "kms:ListGrants",
                "kms:RevokeGrant"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        }
    ]
}
```

### AWS and Symmetric Key

With symmetric key encryption, Bob and Alice use the same encryption key to encrypt and decrypt. In the following case, Bob and Alice share the same encryption key, and where Bob encrypts plaintext to produce ciphertext. Alice then decrypts with the same key, in order to recover the plaintext:

![image](https://asecuritysite.com/public/kms_30.png)


Now we can create a file named 1.txt, and enter some text:

![image](https://asecuritysite.com/public/kms06.png)

Once we have this, we can then encrypt the file using the “aws kms encrypt” command, and then use “fileb://1.txt” to refer to the file:
```
aws kms encrypt  --key-id alias/MySymKey   --plaintext fileb://1.txt   --query CiphertextBlob --output text > 1.out
cat 1.out
```

This produces a ciphertext blob, and which is in Base64 format:
```
AQICAHgTBDpVTrBTrduWKdNnvMoMMUWjObqp+GqbghUx7qa6JwEQ7F2Fzubd+pcz3I06bFuLAAAAdjB0BgkqhkiG9w0BBwagZzBlAgEAMGAGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMgl3vWRVPyL7KK3klAgEQgDP+dQ4KsqT94hiARF8zlybFAtXJJBIucc8M952KHmkJzBGQQP4f8YQQ70DELV97ZXizzME=
```

We could transmit this in Base64 format, but we need to convert it into a binary format for us to now decrypt it. For this we use the “Base64 -d” command:
```
$ base64 -i 1.out  --decode > 1.enc
$ cat 1.enc
```

The result is a binary output:

```
$ cat 1.enc
x:UNSۖ)g
00e0`  1`He.0']3܍:l[v0t *H
]YOȾ+y%3u
D_3&$.q
i        @-_{exddd_v1_w_W3n_145559
```
Now we can decrypt this with our key, and using the command of:
```
$ aws kms decrypt --key-id alias/BillsNewKey --output text --query Plaintext --ciphertext-blob fileb://1.enc > 2.out
$ cat 2.out
```

The output of this is our secret message in Base64 format:

```
VGhpcyBpcyBteSBzZWNyZXQgZmlsZS4K
```

and now we can decode this into plaintext:

```
$ base64 -i 2.out  --decode
This is my secret file.
```

The commands we have used are:
```
aws kms encrypt  --key-id alias/BillsNewKey   --plaintext fileb://1.txt  --query CiphertextBlob --output text > 1.out
echo "== Ciphertext (Base64)"
cat 1.out
echo "== Ciphertext (Binary)"
base64 -i 1.out  --decode > 1.enc
cat 1.enc
aws kms decrypt --key-id alias/BillsNewKey --output text --query Plaintext --ciphertext-blob fileb://1.enc > 2.out
echo "== Plaintext (Base64)"
cat 2.out
echo "== Plaintext"
base64 -i 2.out  --decode
```

and the result of this is:
```
== Ciphertext (Base64)
AQICAHgTBDpVTrBTrduWKdNnvMoMMUWjObqp+GqbghUx7qa6JwEfz+s9z3e0Mw0tOzuB5LuYAAAAdjB0BgkqhkiG9w0BBwagZzBlAgEAMGAGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMqqwXsxB5QlQGVqZWAgEQgDOyBv6KYg4wN2bU/ZKSJ+5opJXMrjQj9GGvuuD2/Jeto9Er5yS91/iCb896CzCSeqUYJeo=

== Ciphertext (Binary)
x:UNSۖ)g
00e0`v0t`He.0'=w*H
yBTVV3b07f'ḫ4#a+$oz
0z%

== Plaintext (Base64)
VGhpcyBpcyBteSBzZWNyZXQgZmlsZS4K

== Plaintext
This is my secret file.
```

Here’s a sample run in an AWS Foundation Lab environment:

![image](https://asecuritysite.com/public/kms07.png)


### Using Python

Along with using the CLI, we can create the encryption using Python. In the following we use the boto3 library, and have a key ID of “98a90e1f-2cb5–4564-a3aa-d0c060cdcf0a” and which is in the US-East-1 region:
```
import base64
import binascii
import boto3

AWS_REGION = 'us-east-1'

def enable_kms_key(key_ID):
    try:
        response = kms_client.enable_key(KeyId=key_ID)

    except ClientError:
        print('KMS Key not working')
        raise
    else:
        return response


def encrypt(secret, alias):
    try:
        ciphertext = kms_client.encrypt(KeyId=alias,Plaintext=bytes(secret, encoding='utf8'),
        )
    except ClientError:
        print('Problem with encryption.')
        raise
    else:
        return base64.b64encode(ciphertext["CiphertextBlob"])


def decrypt(ciphertext, alias):
    try:
        plain_text = kms_client.decrypt(KeyId=alias,CiphertextBlob=bytes(base64.b64decode(ciphertext)))
    except ClientError:
        print('Problem with decryption.')
        raise
    else:
        return plain_text['Plaintext']

kms_client = boto3.client("kms", region_name=AWS_REGION)

KEY_ID = '98a90e1f-2cb5-4564-a3aa-d0c060cdcf0a'
kms = enable_kms_key(KEY_ID)
print(f'KMS key ID {KEY_ID} ')
msg='Hello'
print(f"Plaintext: {msg}")

cipher=encrypt(msg,KEY_ID)
print(f"Cipher {cipher}")
plaintext=decrypt(cipher,KEY_ID)
print(f"Plain: {plaintext.decode()}")
```
    

Each of the steps is similar to our CLI approach. A sample run gives:

```
KMS key ID 98a90e1f-2cb5-4564-a3aa-d0c060cdcf0a 
Plaintext: Hello
Cipher b'AQICAHgTBDpVTrBTrduWKdNnvMoMMUWjObqp+GqbghUx7qa6JwHH797e/TF4csEBEFNmjvD5AAAAYzBhBgkqhkiG9w0BBwagVDBSAgEAME0GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMJf0xVfikbMLfLI6jAgEQgCDYBm2NvB/I2NMxGgSw8wuWA/p6c6Jjm19/wK4eVrLXUw=='
Plain: Hello
```



