<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Test 1
You will answer the questions with either fixed answers, short explainations or with multiple choice. The test is a closed book test, and  runs within the lab time.

Time for test: Wednesday, 1 July, 2:30-4pm. Time: 90 mins.

## Background

* Ciphers and Fundamentals [Link](https://github.com/billbuchanan/csn09112/tree/master/week04_ciphers).
* Symmetric Encryption/Hashing [Link](https://github.com/billbuchanan/csn09112/tree/master/week05_secretkey)
* Public key. [Link](https://github.com/billbuchanan/csn09112/tree/master/week06_public_key/lecture)
* Key Exchange. [Link](https://github.com/billbuchanan/csn09112/tree/master/week06_public_key/lecture)
* Digital Certificates. [Link](https://github.com/billbuchanan/csn09112/tree/master/week07_dig_cert/lecture)

## Test 1 (Challenges)

* Hex Code Challenge [Try](https://asecuritysite.com/Challenges/hex).
* Pigpen [Try](https://asecuritysite.com/Challenges/pigpen).
* Polybius [Try](https://asecuritysite.com/Challenges/polybius).
* Morse [Try](https://asecuritysite.com/Challenges/morse).
* ADFGVX [Try](https://asecuritysite.com/Challenges/dx).
* Scrambled Alphabet [Try](https://asecuritysite.com/Challenges/scramb). Can you beat 5 minutes?

## Test 1 (Examples)

* Rail Code [Try](https://asecuritysite.com/coding/rail).
* Caeser. [Try](https://asecuritysite.com/tests/tests?sortBy=caesar).
* Hex. [Try](https://asecuritysite.com/tests/tests?sortBy=hex01).
* Binary to ASCII. [Try](https://asecuritysite.com/tests/tests?sortBy=ascii02). 

## Test 1 (Some principles)

* Key Enthropy [here](https://asecuritysite.com/encryption/en). How many bits can represent X phases? Just take the Log(X), and divide by Log (2).
* John the Ripper, Hashcat and Ophcrack: [here](http://youtu.be/Xvbk2nSzEPk?t=14m17s)
* Using OpenSSL to salt passwords: [here](http://youtu.be/Xvbk2nSzEPk?t=4m58s)

The table you will use in the test is: [here](https://asecuritysite.com/public/test_table.pdf) and you can use a calculator.

Here are some sample tests:

* [Test 1 (Fundamentals)](https://asecuritysite.com/tests/tests?sortBy=crypto01)
* [Test 2 (Encryption)](https://asecuritysite.com/tests/tests?sortBy=crypto02)
* [Test 3 (Cracking)](https://asecuritysite.com/tests/tests?sortBy=crypto03)

## Study Questions

Try to review your knowledge by answering these questions:

* Can you convert characters from one format to another, such as in binary, hex, ASCII and Base-64 (remember: hex uses four bits at a time, and Base-64 uses six bits at a time)?
* Do you know the basic theory of converting a bit stream into Base-64 (remember 6 bits at a time and convert from table)?
* Do you understand how to use some key ciphers, including shifted alphabet, scrambled alphabet, Vigenere, Pigpen and rail codes?
* Can you do a simple Diffie-Hellman calculation and end up with the same shared key?
* Do you understand how the number of keys relate to the security of the ciphers?
* Can you work out key enthropy, so that if you have 2,048 phases, you can calculate that this is equivalent to 11 bits [log(2048)/log(2)]?
* Would you know how long it would take to crack a code next year, if it takes 10 years now, and computing power doubles each year?
* Do you understand how public and private key encryption is used, along with the usage of digital certificates?
* Do you understand the conversion of passwords into hashed passwords, and use tools such as John The Ripper, Hashcat, Ophcrack and OpenSSL?


# Possible study areas:

* Solve ASCII hexadecimal encoding.
* Solve ASCII binary encoding.
* Solve Morse encoding.
* Solve the shifted alphabet code.
* Create the Vigenere Code for a given plain text string and key.
* Able to convert bit streams to hexadecimal.
* Able to convert binary streams to Base 64.
* Solve Playfair codes.
* Solve Rail codes.
* Solve scrambled alphabet code.
* Calculate the entropy of passwords.
* Calculate simple Diffie-Hellman.
* Determine time to crack a code, on average, given time to test key.
* Determine time to crack a code, for increasing computing power.
* Understands how public key encrypts data.
* Understands how public key is used to provide identity.
* Understands the key elements of a digital certificate.
* Understand the processing of salting a password and its usage in encryption.
* Password hash cracking/salting (LMHASH/MD5).

Tables given are ASCII table, Morse and Base 64.

# What about I know from a practical point-of-view?

The two main labs you should know about are here:

* Lab 5: Crypto - [Lab 5](https://github.com/billbuchanan/csn09112/blob/master/week06_public_key/labs/csn09112_lab05.pdf).
* Lab 6: Crypto - [Lab 6](https://asecuritysite.com/public/csn09112_lab05.pdf).

