<img width="1086" height="214" alt="image" src="https://github.com/user-attachments/assets/e41a66b6-5370-4c19-86ab-dc124b896eeb" />

# Lab 4: Symmetric Key and Hashing

Part 1 Demo: [here](http://youtu.be/HbVenKMGRmE)

We will use OpenSSL for a few tutorial examples. If you want to find out more about the program, discover [here](https://asecuritysite.com/openssl/). 

There are different ways you can do this lab. You will need Ubuntu (or Kali, Parrot or any Debian distro). If using the university's computers, you can either access it via Apporto and GN3, as we did for the labs 1 & 2:

<img width="2869" height="1347" alt="image" src="https://github.com/user-attachments/assets/d00f9944-c43a-4c99-81b6-a1fb14c6ae17" />

Or you can use the ubuntu instance you created in AWS last week:

<img width="2869" height="1347" alt="image" src="https://github.com/user-attachments/assets/2d412dd9-3f11-432a-963c-2241c36f6720" />

If you have your own Windows machine, you may want to install WSL (see last week's appendix for instructions).

Or if you plan on continuing your journey in the world of cybersecurity, you may want to consider installing your own virtual machines with VirtualBox or VMWare (Windows/Linux) or UTM (Mac). Instructions for this can be found in the Appendix and the demonstrators will be happy to help in the JKCC.

Once you have a command line with Ubuntu (or any Debian distro), first check if OpenSSL is installed.

```bash
openssl version
```
<img width="910" height="168" alt="image" src="https://github.com/user-attachments/assets/a7efc59a-5cf1-46a2-8f25-729c46692510" />

If not, install it:

```bash
sudo apt update
sudo apt install -y openssl
```


## A Symmetric Key

| No | Description | Result | 
|-------|--------|---------|
| 1 | Get a terminal open on Linux. |  |
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

### Hashcat Tool

If using Kali or Parrot, hashcat is already pre-installed. If using ubuntu, you need to install it with:

```bash
sudo apt update
sudo apt install -y hashcat
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
EE19033300A54DF2FA41DB9881B4B723
```
Is it [Falkirk][Edinburgh][Glasgow][Stirling]? 


### Q2
Using: [here](http://asecuritysite.com/encryption/md5), determine the number of hex characters in the following hash signatures. 

MD5 hex chars: 

SHA-1 hex chars:

SHA-256 hex chars: 

How does the number of hex characters relate to the length of the hash signature: |

### Q3
The hashes below have been found for the following /etc/shadow file, determine the matching password (the passwords are password, napier, inkwell and Ankle123) - Remember to change the salt!

To find the password, we determine the salt value, and try each password. For example the salt value for ```bill:$apr1$waZS/8Tm$jDZmiZBct/c2hysERcZ3m1``` is ```waZS/8Tm```. To check the password and salt, we can run:

```
openssl passwd -apr1 -salt waZS/8Tm napier
$apr1$waZS/8Tm$jDZmiZBct/c2hysERcZ3m1
```
Now try these ones by trying each of the possible passwords:
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

First you need to get the files

```bash
curl -LO https://raw.githubusercontent.com/billbuchanan/csn09112/master/week05_secretkey/labs/files02.zip
unzip files02.zip -d files02
cd files02
```

the files should have the following MD5 hashes : 

```
MD5(1.txt)= 5d41402abc4b2a76b9719d911017c592 
MD5(2.txt)= 69faab6268350295550de7d587bc323d 
MD5(3.txt)= fea0f1f6fede90bd0a925b4194deac11 
MD5(4.txt)= d89b56f81cd7b82856231e662429bcf2 
```

Which file(s) have been modified: 

Note: Use can use md5sum to compute MD5 hashes.

```bash
md5sum 1.txt
```

### Q5

First you need to get the files

```bash
curl -LO https://raw.githubusercontent.com/billbuchanan/csn09112/master/week05_secretkey/labs/letters.zip
unzip letters.zip -d letters
cd letters
```

View the letters. Are they different? Now determine the MD5 signature for them. What can you observe from the result? 


## C Hashing Cracking (MD5)
Video: [here](http://youtu.be/Xvbk2nSzEPk)


### Q1
Next create a word file (words) with the words of “napier”, “password” “Ankle123” and “inkwell”

```bash
nano words
```

Then create a word file (hash1) with the following hashes

```
232DD5D7274E0D662F36C575A3BD634C
5F4DCC3B5AA765D61D8327DEB882CF99
6D5875265D1979BDAD1C8A8F383C5FF5
04013F78ACCFEC9B673005FC6F20698D
```

Using hashcat crack the following MD5 signatures (hash1):

Command used:
```
./hashcat –m 0 hash1 words
```
232DD...634C Is it [napier][password][Ankle123][inkwell]?

5F4DC...CF99 Is it [napier][password][Ankle123][inkwell]?

6D587...5FF5 Is it [napier][password][Ankle123][inkwell]?

04013...698D Is it [napier][password][Ankle123][inkwell]?


Note: use the --show option to show the results of the cracking.

### Q3
Using the method used in the Q2 part of this tutorial, find the hashes of the following for names of fruits such as "orange", "apple", "banana", "pear", "peach" (the fruits are all in lowercase):

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


## John the Ripper

First, check if you have John installed:
```bash
john --list=build-info
```

If not, install it

```bash
sudo snap install john-the-ripper
sudo snap alias john-the-ripper john
```

### Q1

```bash
john --format=NT --wordlist=words hash.txt
# words is the list of different passwords you need to create/update
# hash.txt is the hashed password you need to create by copy/pasting the hashes below
```

Using John the Ripper, and using a word list with the names of fruits, crack the following pwdump passwords:
```
fred:500:E79E56A8E5C6F8FEAAD3B435B51404EE:5EBE7DFA074DA8EE8AEF1FAA2BBDE876:::
```
Fred's password: 
```
bert:501:10EAF413723CBB15AAD3B435B51404EE:CA8E025E9893E8CE3D2CBF847FC56814:::
```
Bert's password:

### Q2
Using John the Ripper, the following pwdump passwords (they are names of major Scottish cities/towns):

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

## D AWS Cryptography
We are generally moving our security into the public cloud, and thus, many of our keys are stored there. In AWS, we use KMS (Key Management System), and can create either symmetric keys or asymmetric keys (public keys).
In the services dashboard in your AWS learner's lab, select Key Management Service

<img width="2374" height="1234" alt="image" src="https://github.com/user-attachments/assets/7a58fdaa-afb2-4b03-b4a5-79b8861c16eb" />


### Symmetric key

With symmetric key encryption, Bob and Alice use the same encryption key to encrypt and decrypt:

<img width="2008" height="600" alt="image" src="https://github.com/user-attachments/assets/b595120b-c34e-4510-a1fa-fa1592c9914e" />


Normally, we use AES encryption for this. Initially, in KMS, we create a new key within our Customer-managed keys:

<img width="2497" height="1282" alt="image" src="https://github.com/user-attachments/assets/ef1e20bf-4740-4eb4-bdd2-cfc24f389d98" />

and then create the key:

<img width="2868" height="1317" alt="image" src="https://github.com/user-attachments/assets/ef7a0575-ce38-4934-bcc3-de98998383f3" />

Next, we give it a name:

<img width="2868" height="1317" alt="image" src="https://github.com/user-attachments/assets/90fcaa98-33df-4caf-94b3-126df6e9855d" />

And then define the administrative permission (those who can delete it):

<img width="2868" height="1317" alt="image" src="https://github.com/user-attachments/assets/e136ab5b-76ae-42c9-bc4c-30d0723c50c6" />

And the usage:

<img width="2868" height="1317" alt="image" src="https://github.com/user-attachments/assets/68b9ca55-3b82-47c8-9b8f-1313abe25a5f" />

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
        "AWS": "arn:aws:iam::590269919252:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow access for Key Administrators",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::590269919252:role/voclabs"
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
        "kms:CancelKeyDeletion",
        "kms:RotateKeyOnDemand"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Allow use of the key",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::590269919252:role/voclabs"
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
        "AWS": "arn:aws:iam::590269919252:role/voclabs"
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

<img width="2008" height="600" alt="image" src="https://github.com/user-attachments/assets/02cb3093-e6e4-483a-86c9-1fc84c74d800" />

In the Amazon Learners Lab CLI, now we can create a file named 1.txt, and enter some text:

<img width="2868" height="1317" alt="image" src="https://github.com/user-attachments/assets/c8548441-932b-47a2-be33-46e37eade923" />


Once we have this, we can then encrypt the file using the “aws kms encrypt” command, and then use “fileb://1.txt” to refer to the file:
```bash
aws kms encrypt  --key-id alias/MySymKey   --plaintext fileb://1.txt   --query CiphertextBlob --output text > 1.out
cat 1.out
```

This produces a ciphertext blob, and which is in Base64 format:
```bash
AQICAHgTBDpVTrBTrduWKdNnvMoMMUWjObqp+GqbghUx7qa6JwEQ7F2Fzubd+pcz3I06bFuLAAAAdjB0BgkqhkiG9w0BBwagZzBlAgEAMGAGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMgl3vWRVPyL7KK3klAgEQgDP+dQ4KsqT94hiARF8zlybFAtXJJBIucc8M952KHmkJzBGQQP4f8YQQ70DELV97ZXizzME=
```

We could transmit this in Base64 format, but we need to convert it into a binary format for us to now decrypt it. For this we use the “Base64 -d” command:
```bash
base64 -i 1.out  --decode > 1.enc
cat 1.enc
```

The result is a binary output:

<img width="1128" height="153" alt="image" src="https://github.com/user-attachments/assets/e2efd217-aae9-428a-8998-b0f7b2b646f3" />


Now we can decrypt this with our key, and using the command of:
```bash
aws kms decrypt --key-id alias/MySymKey --output text --query Plaintext --ciphertext-blob fileb://1.enc > 2.out
cat 2.out
```

The output of this is our secret message in Base64 format:

```
VGhpcyBpcyBteSBzZWNyZXQgZmlsZS4K
```

and now we can decode this into plaintext:

```
base64 -i 2.out  --decode
```

<img width="1653" height="177" alt="image" src="https://github.com/user-attachments/assets/d29a954a-8016-471a-9e34-233818883531" />


The commands we have used are:
```
aws kms encrypt  --key-id alias/MySymKey
cat 1.out
echo "== Ciphertext (Binary)"
base64 -i 1.out  --decode > 1.enc
cat 1.enc
aws kms decrypt --key-id alias/MySymKey --output text --query Plaintext --ciphertext-blob fileb://1.enc > 2.out
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

<img width="2182" height="1134" alt="image" src="https://github.com/user-attachments/assets/7724d219-171f-40da-8b53-c68b77b764eb" />

### Using Python

Along with using the CLI, we can create the encryption using Python. In the following, we use the boto3 library, and have a key ID of “MySymKey” and which is in the US-East-1 region:

First, create the python file:

```bash
nano kms_encrypt.py
```

And in it paste in this code

```python
import base64
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-1'

KEY_ALIAS = 'alias/MySymKey'

kms_client = boto3.client("kms", region_name=AWS_REGION)


def encrypt(secret, key_id):
    try:
        response = kms_client.encrypt(
            KeyId=key_id,
            Plaintext=bytes(secret, encoding='utf8'),
        )
    except ClientError:
        print('Problem with encryption.')
        raise
    else:
        return base64.b64encode(response["CiphertextBlob"])


def decrypt(ciphertext, key_id):
    try:
        response = kms_client.decrypt(
            KeyId=key_id,
            CiphertextBlob=bytes(base64.b64decode(ciphertext)),
        )
    except ClientError:
        print('Problem with decryption.')
        raise
    else:
        return response['Plaintext']


print(f'Using KMS key: {KEY_ALIAS}')

msg = 'Hello'
print(f"Plaintext: {msg}")

cipher = encrypt(msg, KEY_ALIAS)
print(f"Cipher: {cipher}")

plaintext = decrypt(cipher, KEY_ALIAS)
print(f"Plain: {plaintext.decode()}")
```

Then run it
```bash
python3 kms_encrypt.py
```

Each of the steps is similar to our CLI approach. A sample run gives:

<img width="1794" height="292" alt="image" src="https://github.com/user-attachments/assets/825b2711-4d89-40ee-bfd8-c9671b4b36db" />

### Optional: Create a vault for your keys

In this part of the lab, we will solve a big security issue we created during Lab 3.

In the AWS lab, we created a key pair, and we downloaded it. This is problematic. Anyone with access to your computer could easily read this in the clear. And attackers particularly value file extensions such as `.pem` knowing that it will allow them further access.

How do we solve this? By creating a vault.

You have seen in class how Symmetric Keys work. Now let us see them being used in practice.

Firstly, on Ubuntu (or Kali, or Parrot), you need to install gocryptfs (and OpenSSL, if you have not yet done it, see above for instructions)

```bash
sudo apt install gocryptfs
```

Next, we need to create the directories that will be used as our vault, alongside a mounting point
```bash
mkdir vault open_vault
```

You always need two folders:
`vault` holds the encrypted data on disk. It is always there, always encrypted.
`open_vault` is the window into it. It is empty when locked and shows plaintext when mounted.

Then we need to initialise the vault with a password. Your vault will only be as secure as the password used to protect it!
```bash
gocryptfs -init vault
```
gocryptfs also prints a master key. Note it down somewhere safe -not on the computer!-, because it's your only way back in if you forget the password.

Now we will create an OpenSSL keypair (which will give us the same .pem file type than the one we got from AWS)
```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private.pem
openssl pkey -in private.pem -pubout -out public.pem
#then check your key
cat private.pem
```

Now we need to mount the vault, made possible by giving the password
```bash
gocryptfs vault open_vault
```

Now the vault is a directory in our Linux system, we can move the private key in it:
```bash
mv private.pem open_vault/
# Check that the key is there and unencrypted
ls open_vault
cat open_vault/private.pem
```

Now lock your vault! The following action will make open_vault an empty directory. 
```bash
umount ~/open_vault
```
And you can see the encrypted data in the vault:
```bash
cd vault
# you will notice your private.pem file has been turned into random Base64
cat <whichever base64 your file has>
# you should be enable to make any sense of the encrypted file, as per the screenshot below
# and check that open_vault is empty
cd ..
ls -la open_vault
```

<img width="1221" height="805" alt="image" src="https://github.com/user-attachments/assets/512035d7-318e-4c20-81ec-108c7367c3a5" />

And if you need to get your data back, open your vault!
```bash
gocryptfs vault open_vault
cat open_vault/private.pem
```

And as a finishing touch, research what Symmetric key scheme is being used by gocryptfs, and which hashing scheme is used to protect the password, do you think it is safe? What sort of attack would ever have a chance to break into your vault?




### Appendix

Installing your own virtual lab on your own computer.

Windows & Linux

You can install VirtualBox
https://www.virtualbox.org/wiki/Downloads

Next, download the image of any of the following distros (select virtualbox image):

https://www.kali.org/get-kali/#kali-virtual-machines 
https://www.parrotsec.org/download/
https://www.osboxes.org/ubuntu/

Choose whichever one you prefer. Kali and Parrot both come with all the security tools installed, but each tool can be installed on a Ubuntu with a single command line, so it is really up to you which distro you want to use. 

Once your image is downloaded, unpack it if it is zipped

<img width="2025" height="384" alt="image" src="https://github.com/user-attachments/assets/65ad57ff-61f2-49e1-8d28-99c373bb3bd3" />

And open it in VirtualBox

<img width="3128" height="1690" alt="image" src="https://github.com/user-attachments/assets/de787467-6045-47de-93d8-7b5abe00f9bb" />

Then in the Settings, in the System tab, in Memory, use as much as your system can be comfortable with (It will run on 2GB, but 4GB may make it more stable.)

<img width="1658" height="1216" alt="image" src="https://github.com/user-attachments/assets/00310a3d-fcc6-4663-a999-c67df0eba743" />

Similarly, give as many cores of cpu as your system can comfortably give. 

<img width="1658" height="1216" alt="image" src="https://github.com/user-attachments/assets/6838738b-599f-4d35-885c-710d6f9bdf51" />

Click ok and start your new machine.

For Kali, username and password is kali, for Parrot user / toor, and Ubuntu via osboxes is osboxes / osboxes.org

<img width="1656" height="1428" alt="image" src="https://github.com/user-attachments/assets/a3c7ea72-4ae3-47ec-b652-0aaa0bf5a449" />

And that's it! You can now follow the lab's instruction within your own VM! Later on you may want to add more machines and experiment with creating a whole network with intentionally vulnerable nodes, but this is beyond the scope of this module.



#### Alternative for Mac

If using a Mac, VirtualBox is an option, but you may want to use UTM instead:

https://mac.getutm.app/

Handily, it comes with direct links to popular virtual machines images directly via its GUI, in the UTM Gallery. 

