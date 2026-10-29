# Creating ML-Keys
With ML-KEM, Bob creates a secret to share with Alice. He will encapsulate it with Alice's ML-KEM public key, and then she will decapulate it with her ML-KEM private key:

<img width="1393" height="925" alt="image" src="https://github.com/user-attachments/assets/2e63a007-72a9-47c7-85d4-da86de50fb17" />

Initially Alice define the AWS region, and creates an ML-KEM-768 key pair in the KMS:

```
~ $ export AWS_DEFAULT_REGION=us-east-1
~ $ aws kms create-key  --key-spec ML_KEM_768 --key-usage ENCAPSULATE_DECAPSULATE --description "ML-KEM-768 keys"
{
    "KeyMetadata": {
        "AWSAccountId": "XXXXXXXXXXX",
        "KeyId": "abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25",
        "Arn": "arn:aws:kms:us-east-1:103269750866:key/abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25",
        "CreationDate": "2026-10-29T20:27:26.425000+00:00",
        "Enabled": true,
        "Description": "ML-KEM-768 keys",
        "KeyUsage": "ENCAPSULATE_DECAPSULATE",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "ML_KEM_768",
        "KeySpec": "ML_KEM_768",
        "EncapsulationAlgorithms": [
            "ML_KEM"
        ],
```
Now we can extract the public key with:

```

~ $ aws kms get-public-key  --key-id "abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25"  --query PublicKey  --output text
MIIEsjALBglghkgBZQMEBAIDggShAInpfQW0pxGUyPT8UsibDolSuKfRIOnHgn1HksJQTzAlRu4krxvTKlrZfFMcpzuxK/35FCV8ziXkYqYhZF/KxqahsWMnN4awd8lzg7iiG+b6vayjDHk2HVopZFmKfKEzqjSpsIn4i4yXE+rBo3sLNhGWtt2rhhMAF9KHxWV7jqgIAoc0CbJEWTJbgPC7ClP7QyAiB/QabVu6cmUogSN7T1nVobeQNGSKkf7YnI0olrJkBH3mEHzqWBBHM5nVOqfAlklhYxp5KFjVgQSMTz7sMmQDIbvXkKTJzn9rSzDxNGRqPeCir3MFb/S4q0O4c2qCH4/ABXGaAZh8LqNhFpByzirRJhxByfa6hb6cyjW4YKnSwSYVRD3cvWUnzfJ2p4CznLSbOhhDJhOqc/yUCzpJEwioWouSiMRah1jVag67DKuiy5J8BL8xAWR7JrzqeagiEkDiTS2yazEros4GEYGweKv7OUoAnIE1Y350USRojGIcaC8jxHOSePzpnWHQzOC0KWqEwNqHa3cwh7tcC5NKROnUOzF5GH7JKa2hGCjrGIYSYxuIfW6ZSH74U3UEO/KTQBLCj8IEOzbTJeBptSlGCxQRJxrKgF5IAFpnIKDoJGHBF9aVGevimWzLmSaKateUUBhyf0kBpbWMg6AqXG7Iw6PizbwMn5eWIYdgBXLJsHvsyb5HlgRZuynZHP8gWQo0SXZsSO3WCnJZoCOqPR2xpIMgK2E1PlhSlrkwjb0IH96oHltBAz9kOgtVhypMhkOssNeYDfKKQgbXWKBjtn3gfJwrFDUaxG3XgCtKQxZ6w9NJeDi1Ejvnkwt4rJPJXsX8Z9V5Gj/pfGfVOhnVzCRgq5i8DloDN+9SuC2Wrse1dQtyM7vSadHsCztHkBWbPXn6bzrlgLTyxdnheIOiFLdCo+nBMaMlXQh5xuRYF5p5kKqYSyomq8lwq+BJoCwlqFjyO9QqxKX4jHHZbQHRXr80ocIaUcBXd7iJGsZ6reV8YnpWYmF1CWr5w6vrU1mJAKvsEAmcAveCa1PKLqRaD7KHLezFsUU3ziQAo6bRlYfsanSwDzH8tdaEsTf5XzkQsf76yLkBA9TQv1apTwb7uqyLImIMR/K4LERbtLxctHT7ynDAGOryD/GZJ6W7dAZrALoGXjiQWXRUi6XhQpxXthcEBGB3w2y1XhRLUaOVJZRKMxr5GL7WbD0XA3R0VaGMKWlBYrf8t+vTzodqFflQaXiAxlHEwieQsVhWy9FxYZZUlK+Wvn/3mBexWQ5CKY9ViyHneu5pDAiCzb3iJRtTwjW6kTZUWfM8iihlfqr2gw3KnQ3wxrQsS+hXOHZRCmsTrBHka7PHltJDywqXpki4mk1BUY1GsZGYns48r/dJpoIMWqsGre61qwDweYcokxxXB18bsvxBN7YhS3npiv87PKbViMHCkMACQ/0DRvLXWQPAVwmneK45dChceo8QWyP1BFDMJGSHaYGqfUjyfXmHPqgAXSC1zrEmtAZ6bm32fJrLdaNKQ0DrVtZsc3U5kLMhtsCxiLygkErBQ0ZpetFcZRGABL56DXPXb7TAZpPRXWvH38UZ
```

This is a Base-64 format, but can also create a binary format with:

```
~ $ aws kms get-public-key  --key-id "abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25"  --query PublicKey  --output text | base64 --decode > mypublic.der
```
Next we can ensaplate a secret key using the public key:

```
~ $ aws kms encapsulate  --key-id "abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25"   --encapsulation-algorithm ML_KEM  --output json > encapsulated.json                                                        
~ $ cat encapsulated.json 
{
    "KeyId": "arn:aws:kms:us-east-1:103269750866:key/abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25",
    "SharedSecret": "xlnZBlCguX0YQ/6CrhljK8vid3rB0RjLmnNOfr9UZkQ=",
    "SharedSecretCiphertextBlob": "UTEbiwXXvxCq1qkNm9sYPW3ATuf63JQ/hhkOKrMrvYokHRQD/EK7S0hse+2ZIIQjW0g4bf5zdVwiMtI/1oqetm83T+zDkorQFkREV4Zq0YTPZBFPiD7CagGE8XjHvxFO9PdsNTxJPFjP5VDw4wNNGLfiuUMDupcF5bm4QWmOZ/iWjVoFlNJc4AvO5b6GLR3YVqoudRGqPmUpNe6g+dClCrkiPLBW8sJnmZElMJF9RfTe0z3b6ltGzKKPW/1raLHS+BCxxJdYXptXW467bWqeSSZHhbdQlwDtwfSj/CjoZoJlpBASiPQIYnrSHA6iMzEFglXC0zymkiu9Yb4Qr3nLbq0nqUx2zFx/MxIUZbkkY4x+Vl+P5zxyQT32joGzTDNc8Yx+81pCBZ9ZkE42+IHXqXiNTh/Y0FWKDb8MY7645K49vmKABbclEziBNUHKbVzSH7xFE6OzmBbqO1+UiFVCqSAacDxi4XDmYZgSCABNcSDrRNhHMM1g7X+hg7+TgbSAg7KnZVkuCwMrsZiLdlPjElBWaYiTFk3yFEO0G5iFUqWEycyAM8z4FtezDcBt7w0mkFMVxClBzYYqKjp523AJdBKKZBnpB4X1dDe6C59NqV8jIH+h9TuUcuCD+thQ5eCg8vQ28N5xyU/k5hgNXvjOuVnHXa+JgjP3WLiIqNGNhzIuKNjjALbwa6k86kQJy/muWjfEMsd+Rv7/m2dRS0w5/DFW6FHNGostwlB3bH9uO8jht8wtPf3fySOOmKN7lzeEYj6b9pCUNvxsmSVRZx9GFYwKjMIDEVFzjcdY//mUNo6IjzAKsYGRZtkAlnCT3x8H7ifXgxmuEsJ9XU4HHIuDBADs8uN51VM7URk82gGE0hnpdgfrW1cTS7ZFPJdPwUKdxkAfHVMpvWiWDTASZkeSR2bFj/qtRx0Wz+es5JD5uhtKmoQKQTn1vvU3SdcLOCjCqQqievYsEFRaLHdiO0J60rKkCGks6R+x7pe13Iv2TzDnu/3LVAgOLXaeOvvEeYqKtYPGSac/en5CVgWGmjjFYZQNp8VK5wQqeBZKjf0eZeQd/3tBOOjLaRKDWJpeTDgBCFwckoYa4SPI3rvJmk5p2LE3PIWjQ5m0OphANY85F60na5exvJxzoZA+MaX1ygUpNHK71gmQePYHdyKzb2FlwV3v45vQQmzR4gA763/OEMXAdm4uuqmrf31LwiPMlwiwnpRC76NQjn2jPjlWTA6BRn9LfPpNiOrb1WcBnesQFbRiD9mRcUwTKQE3kMcdf+5vwbHSRr68/xjC821Mg61fjKd2ZbdoiKPiznHCTnIE8m1rZYy0cwfXYI5wPg/hFlM/2GD5appVbdcqiMD4Kh1Agxxr1wZdvgrKzRr0vfLE0OWcyQRrD5voN+ia3MAwhN2o4fsFC4PBnTAh1VsgpZvPXojK2wT+sB3zh/19iXkuMBc=",
    "EncapsulationAlgorithm": "ML_KEM"
}
```

We can now extract the secret key with:

```
~ $ jq -r '.SharedSecret' encapsulated.json   | base64 --decode > secret1.bin
```

And the ciphertext to send to the other side:

```
~ $ jq -r '.SharedSecretCiphertextBlob' encapsulated.json   | base64 --decode > ciphertext.bin
```

Once the ciphertext is received, it can be decapulated in the KMS with the private key:

```
~ $ aws kms decapsulate  --key-id "abcf3ac4-3dbe-43c0-947f-25ca1c3a8b25"    --encapsulation-algorithm ML_KEM    --shared-secret-ciphertext-blob fileb://ciphertext.bin    --query SharedSecret    --output text | base64 --decode > secret2.bin
```

If we compare the secrets we get:

```
~ $ cmp secret1.bin secret2.bin && echo "ML-KEM SUCCESS"
ML-KEM SUCCESS
```
and can also discover the secret keys on either side:
```
~ $ cat secret1.bin | base64
xlnZBlCguX0YQ/6CrhljK8vid3rB0RjLmnNOfr9UZkQ=
~ $ cat secret2.bin | base64
xlnZBlCguX0YQ/6CrhljK8vid3rB0RjLmnNOfr9UZkQ=
```
