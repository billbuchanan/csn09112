<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Lab 5: Diffie-Hellman and Public Key

Part 1 Demo: [here](http://youtu.be/HbVenKMGRmE)

We will use OpenSSL for a few tutorial examples. If you want to find out more about the program, discover [here](https://asecuritysite.com/openssl/).

## 1	Diffie-Hellman

| No | Description | Result | 
| -------|--------|---------|
| 1 | Bob and Alice have agreed on the values: <br/>g=2,879, N= 9,929 Bob Select b=6, Alice selects a=9 | Now calculate (using the Kali calculator): <br/>Bob’s B value (g<sup>b</sup> mod N): <br/>Alice’s A value (g<sup>a</sup> mod N): |
| 2 | Now they exchange the values. Next calculate the shared key: | Bob’s value (A<sup>a</sup> mod N):	Alice’s value (B<sup>a</sup> mod N): Do they match? [Yes] [No] |
| 3 | If you are in the lab, select someone to share a value with. Next agree on two numbers (g and N).  | You should generate a random number, and so should they. Do not tell them what your random number is. Next calculate your A value, and get them to do the same. Next exchange values. | Numbers for g and N: <br/>Your b value: <br/>Your B value:  <br/>The A value you received: <br/>Shared key: <br/>Do they match: [Yes] [No] |




## 2 Public Key

| No | Description | Result | 
| -------|--------|---------|
| 1 | First we need to generate a key pair with: openssl genrsa -out private.pem 1024	This file contains both the public and the private key. | What is the type of public key method used: How long is the default key: How long did it take to generate a 1,024 bit key? View the contents of the keys. |
| 2 | Use following command to view the output file: cat private.pem | What can be observed at the start and end of the file: |
| 3 | Next we view the RSA key pair: openssl rsa -in private.pem -text -noout | Which are the attributes of the key shown: Which number format is used to display the information on the attributes: What does the –noout option do? |
| 4 | Let’s now secure the encrypted key with 3-DES: openssl rsa -in private.pem -des3 -out key3des.pem | |
| 5 | Next we will export the public key: openssl rsa -in private.pem -out public.pem -outform PEM -pubout  | View the output key. What does the header and footer of the file identify? |
| 6 | Now we will encrypt with our public key: openssl rsautl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin | 
| 7 | And then decrypt with our private key: openssl rsautl -decrypt -inkey private.pem -in file.bin -out decrypted.txt	| What are the contents of decrypted.txt |
| 8 | If you are working in the lab, now give your password to your neighbour, and get them to encrypt a secret message for you. | Did you manage to decrypt their message? [Yes][No] |


## 3	Storing keys
We have stored our keys on a key ring file (PEM). Normally we would use a digital certificate to distribute our public key. In this part of the tutorial we will create a crt digital certificate file.

| No | Description | Result | 
| -------|--------|---------|
| 1 | Next create the crt file with the following: openssl req -new -key private.pem -out cert.csr  openssl x509 -req -in cert.csr -signkey private.pem -out server.crt | View the CRT file by double clicking on it from the File Explorer. What is the type of public key method used: View the certificate file and determine: The size of the public key: The encryption method: |
| 2 | We can now take the code signing request, and create a certificate. For this we sign the certificate with a private key, in order to validate it:<br/>openssl x509 -req -in cert.csr -signkey private.pem -out server.crt | From the File System, click on the newly created certificate file (server.crt) and determine:<br/>The size of the public key (in bits): [512][1024][2048]<br/>The public key encryption method:<br/>Which is the hashing method that has been signed to sign the certificate: [MD5][SHA-1][SHA-256] |

## 4 AWS: Public Key Encryption
In the following figure, Bob uses Alice’s public key to encrypt data, and which creates ciphertext. Alice then decrypts this ciphertext with her private key:

<p><img src="https://asecuritysite.com/public/kms_10.png" width="750px" />
	
 <p>If we use asymmetric keys, we typically just have the choice of using RSA to encrypt and decrypt data. This is because elliptic curve cryptography does not naturally support encryption and decryption, and we must use hybrid methods (such as with ECIES).

### Creating an RSA key pair in AWS

Now, let’s create an RSA key pair for encrypting a file. Our keys are contained in the KMS:

<img src="https://asecuritysite.com/public/kms_11.png" width="750px" />

Initially, we can create a Customer-managed key pair with:

<img src="https://asecuritysite.com/public/kms_12.png" width="750px" />

The options are 2K, 3K or 4K RSA key pairs. Next, we can give the key an alias:

<img src="https://asecuritysite.com/public/kms_13.png" width="750px" />

Then define the ownership of the keys:

<img src="https://asecuritysite.com/public/kms_14.png" width="750px" />

And finally the permissions:

<img src="https://asecuritysite.com/public/kms_15.png" width="750px" />

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
                "AWS": "arn:aws:iam::222222:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow access for Key Administrators",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::222222:user/asecuritysite"
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
                "AWS": "arn:aws:iam::222222:user/asecuritysite"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:DescribeKey",
                "kms:GetPublicKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow attachment of persistent resources",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::222222:user/asecuritysite"
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

Once created, we cannot access the private key, but will be able to view the public key:

<img src="https://asecuritysite.com/public/kms_16.png" width="750px" />

We can download this from the console, or from the command prompt:

```
% aws kms get-public-key --key-id alias/PublicKeyForDemo
{
    "KeyId": "arn:aws:kms:us-east-1:103269750866:key/de30e8e6-c753-4a2c-881a-53c761242644",
    "PublicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsXDtHOdCeteObzugPf6ENjeft6CDGjbaR9t40++q4jqtSd5JsdYel1Rn3mYL+oXqKQJz9o+aoXdCcMFkhu6wqqDVbIOPT2nsXIuO3p+0G7uUS93g3cc5RodEAn3jb2yBjHjvfs9OBSBM7bh6Kw21YuN/omU1GaL/d4o7+NYu0mDEAmb0Nh+1Q6lrpf+bu1YZ31gVpbLd78xGlv1dz2nqyBG8VaZW90fr05jDjcpDnWm1O9QXl0pEhwNGcvcsxcHodslAZrlzKUre/nZ5MTNL3uigw8w5l2uQLRFiIBpLlHKpcNBaxZu3Za5Mk2Dvj+1+L2PejLydAPfqQB5N8dsOAQIDAQAB",
    "CustomerMasterKeySpec": "RSA_2048",
    "KeySpec": "RSA_2048",
    "KeyUsage": "ENCRYPT_DECRYPT",
    "EncryptionAlgorithms": [
        "RSAES_OAEP_SHA_1",
        "RSAES_OAEP_SHA_256"
    ]
}
```

### Encrypting with the public key

We can now create a file (1.txt):

<img src="https://asecuritysite.com/public/kms_17.png" width="750px" />

And now encrypt using RSA with OAEP padding (RSAES_OAEP_SHA_1):
```
$ aws kms encrypt  --key-id alias/PublicKeyForDemo   --plaintext fileb://1.txt  --query CiphertextBlob --output text --encryption-algorithm RSAES_OAEP_SHA_1 > 1.out 
```
This will create a Base64 output of the encrypted file (1.out). We can list the file with:

```
% cat 1.out
nORNC8PQotPOpf7R1XlCaz8pQKEn5k6r3VOvLZk9ipzl7mGwV25HVqDc/ocK58eV/3u8IQVZDK81UPxk7D1BSc5LN5lvtxnIx8G7TfePxTDuu2+EM5zavvU2S/2ZS+DOV2yHthHfNRKSDLB8a9oMzKBNcsfZBLGZEeZxEs/Rt5T7NdwWXnQsXbrgBJnvbfnNTzgyY4lPLjNqS4DPjA4UVI/3ICUjsEdKNvOv3XebBFvRaJ1a3flBJM5Bxo73gJSidwEZgTPSvGVdA5KOxoDuFh6gPmr/ztRirrrmkjF6zbdWlRfaNb9pLipvZz4KyDUkkKH0v2iYb+zAWzemuZ47sw==
```

This can be transmitted or stored. But, if we want to decrypt this, we need to convert the Base64 encoded data into binary:
```
$ base64 -i 1.out  --decode > 1.enc
```

Now, if we list 1.enc we see that it has binary data:
```
$ cat 1.enc
M
ТΥyBk?)@@'NS-=aWnGV
Ǖ{!Y
5Pd=AIK7oM0o3ھ6KKWl5
|k
̠Mrqѷ5^t,]mO82cO.3jKόT %#GJ6w[hZA$AƎw3Ҽe]ƀ>jb1zͷV5i.*og>
5
```
### Decrypting with the private key

Now to decrypt the file (1.enc) with the associated private key. For this, we use:
```
$ aws kms decrypt --key-id alias/PublicKeyForDemo --output text --query Plaintext --ciphertext-blob fileb://1.enc --encryption-algorithm RSAES_OAEP_SHA_1 > 2.out
```

This produces an output file of 2.out. Again, this is in a Base64 format:
```
$ cat 2.out
VGhpcyBpcyBteSBzZWNyZXQgZmlsZS4K
```
so we need to decode this with:
```
$ base64 -i 2.out  --decode
This is my secret file.
```
And, that’s it. Note that the two main encryption methods we can use (with padding) are OEAP SHA-1 and OAEP SHA-256:
<img src="https://asecuritysite.com/public/kms_18.png" width="750px" />


### Using Python
We can use the same type of approach with Python. In the following case we use boto3, select an RSA key pair, and add the option of EncryptionAlgorithm='RSAES_OAEP_SHA_1' for the encryption and decryption:

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
        ciphertext = kms_client.encrypt(KeyId=alias,EncryptionAlgorithm='RSAES_OAEP_SHA_1',Plaintext=bytes(secret, encoding='utf8'),
        )
    except ClientError:
        print('Problem with encryption.')
        raise
    else:
        return base64.b64encode(ciphertext["CiphertextBlob"])


def decrypt(ciphertext, alias):
    try:
        plain_text = kms_client.decrypt(KeyId=alias,EncryptionAlgorithm='RSAES_OAEP_SHA_1',CiphertextBlob=bytes(base64.b64decode(ciphertext)))
    except ClientError:
        print('Problem with decryption.')
        raise
    else:
        return plain_text['Plaintext']

kms_client = boto3.client("kms", region_name=AWS_REGION)

KEY_ID = '68ded69b-6c19-4b34-9f91-f8c2628ee612'
kms = enable_kms_key(KEY_ID)
print(f'Public Key KMS ID {KEY_ID} ')
msg='Hello'
print(f"Plaintext: {msg}")

cipher=encrypt(msg,KEY_ID)
print(f"Cipher {cipher}")
plaintext=decrypt(cipher,KEY_ID)
print(f"Plain: {plaintext.decode()}")
```
A sample run gives:
```
KMS key ID 68ded69b-6c19-4b34-9f91-f8c2628ee612
Plaintext: Hello
Cipher b'SvUOFgRLjpekJn1ZDuivW7YP3mCz3dCGwiWzaekrmcKhDyQbAh7wkBlr0ShC5xjJyC+jJ/0SdcXlKkbzWe8W/EfmKgo8zGcHsiil2F1d6fT9veGxO75ySWz9uwVuoqnsJ0Z32dJG/7nlrGECNU9z984r2cLwiIidgKtqKm2bo48EguVUrU/GuNntxOV0u88r7GShpn6oZV3NPaPOhGEBTpCMGq8nXbv81H6fMWsG92kbVW8PcOqM7cSw0z+XSaj/ndiKzD3yostib+drVtLPOJJ/idBXtOnKPMPEyiKAhMFUxYn+qk104egf5xn6Swh9nU1sogP4Xg0yBT6TdWQACg=='
Plain: Hello
```


### Conclusions

And, that’s it. RSA can be used to encrypt and decrypt data, and where we encrypt with the public key and decrypt with the private key. Thus, anyone who has our public key can encrypt data for us, and for us to decrypt it with our private key. Normally RSA is not used when we have large amounts of data, and a typical use case is to encrypt a symmetric key.

One thing to watch is that the usage of the keys needs to be locked down to certain users and that the owner of the keys needs to be carefully controlled, as, if someone deletes your keys, you will possibly not be able to decrypt files that have been encrypted with those keys. Luckily, there is a 7–30 day time window for a key to be deleted — just in case you have deleted it by mistake, or if someone has maliciously deleted it:
<img src="https://asecuritysite.com/public/kms_19.png" width="750px" />


# 5 Python tutorial
For this part of the lab, install:

```
pip install pycryptodome
```

In Python, we can use the Hazmat (Hazardous Materials) library to implement symmetric key encryption. 

Web link (Cipher code): [here](http://asecuritysite.com/cipher01.zip)

The code should be:

```
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import sys
import binascii

val='hello'
password='hello123'

plaintext=val

def encrypt(plaintext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

key = hashlib.sha256(password.encode()).digest()

print("Before padding: ",plaintext)

plaintext=pad(plaintext.encode())

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext)))

ciphertext = encrypt(plaintext,key,modes.ECB())
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())
```

How is the encryption key generated?

Which is the size of the key used? [128-bit][256-bit]

Which is the encryption mode used? [ECB][CBC][OFB]

Now update the code so that you can enter a string and the program will show the cipher text. The format will be something like:
```
python cipher01.py hello mykey
```
where “hello” is the plain text, and “mykey” is the key. A possible integration is:
```
import sys

if (len(sys.argv)>1):
	val=sys.argv[1]

if (len(sys.argv)>2):
	password=sys.argv[2]
```

Now determine the cipher text for the following (the first example has already been completed):

| Message |	Key | CMS Cipher |  
| -------|------|------|
| “hello” |	“hello123” |	0a7ec77951291795bac6690c9e7f4c0d |
| “inkwell”|	“orange”	| |
| “security”|	“qwerty”	||
| “Africa” |	“changeme”	||

Finally, change the program so that it does 256-bit AES with CBC mode.







