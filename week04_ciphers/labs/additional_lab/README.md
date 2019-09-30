
<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>
<h1>Network Security and Cryptography (Software Tut 2)</h1>

<p>This is an introduction to Python coding for ciphers.<p>
<h2>GCD</h2>

Within cryptography we often have to present numbers in different formating, and typically have to convert from decimal into hexadecimal (based 16). Enter the following Python program:

<pre>
def gcd(a, b):
	while( b != 0 ):
		Remainder = a % b;
		a = b;
		b = Remainder;
	return a;

g = gcd(54,8)
print g
</pre>

<p>Now use it to complete determine the following:</p>
<ul>
<li>The GCD of 4032 and 76?</li>
<li>The GCD of 9999 and 77?</li>
<li>The GCD of 125 and 32?</li>
 </ul> 

<h2>Ciphers</h2>
<p>1. Morse code is a simple substitution cipher. Implement some Python code which allows the user to enter a word, and the program should convert it into Morse code. Some reference code can be found <a href="https://gist.github.com/guinslym/ebb4fefe0f7d63beab01a70a8fd630d7" target="_blank">here</a>. Using your program, decipher the following:
	
<pre>
(—···) (— — —) (—··—) (·) (···) 		
(·—) (·—·) (·—·) (·—) (—·— —) 		
(···) (·) (·—·) (···—) (·) (·—·) 		
(—·—·) (·—··) (··) (·) (—·) (—) 
</pre>

2. With the Caesar cipher we can shift the plaintext alphabet by one of 25 combinations. Create a Caesar cipher program which will shift a plaintext or a ciphertext word by each of the 25 shifts. A sample run is given below:

<pre>
Shifts	Back	Result
-------------------------
0	[26]	LIPPS
1	[25]	MJQQT
2	[24]	NKRRU
3	[23]	OLSSV
4	[22]	PMTTW
5	[21]	QNUUX
6	[20]	ROVVY
7	[19]	SPWWZ
8	[18]	TQXXA
9	[17]	URYYB
10	[16]	VSZZC
11	[15]	WTAAD
12	[14]	XUBBE
13	[13]	YVCCF
14	[12]	ZWDDG
15	[11]	AXEEH
16	[10]	BYFFI
17	[9]	CZGGJ
18	[8]	DAHHK
19	[7]	EBIIL
20	[6]	FCJJM
21	[5]	GDKKN
<b>22	[4]	HELLO</b>
23	[3]	IFMMP
24	[2]	JGNNQ
25	[1]	KHOOR
</pre>

Using your program, can you find the plaintext for the Caesar cipher of "SQDYMZK"?

3. The homomorphic substitution cipher tries to make each cipher code occur with the same frequency. Write a program which creates the homorphonic substitution cipher for the following cipher mapping:

<pre>
a   b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
07 11 17 10 25 08 44 19 02 18 41 42 40 00 16 01 15 04 06 05 13 22 45 12 55 47
31 64 33 27 26 09 83 20 03       81 52 43 30 62    24 34 23 14    46    93
50    49 51 28       21 29       86    80 61       39 56 35 36            
63       76 32       54 53       95    88 65       58 57 37   
66          48       70 68             89 91       71 59 38   
77          67       87 73                94       00 90 60   
84          69                            96             74   
            72                                           78   
            75                                           92   
            79                                                
            82 
            85

</pre>

4. The Baudot code uses a 5-bit conversion from English characters. Based on the code below, write a Python program which converts plaintext into a cipher stream of bits:

<pre>
        public string baud(string str)
        {
            string[] conversion = new string[] {"*", "E","%", "A", " ", "S", "I", "U","\r", "D",
            "R", "J", "N", "F", "C", "K", "T", "Z", "L", "W",
            "H", "Y", "P", "Q", "O", "B", "G",  "", "M", "X",   
           "V", ""};
            if (str==null) return("");
            string result = "";
            str = str.ToUpper();
            foreach (char ch in str)
            {
                string ch2 = ch.ToString();
                int ptr = 0;
                foreach (string ch1 in conversion)
                {
                    if (ch2 == ch1) result += "[" + ptr + "-"+GetBinaryString(ptr)+ "]";
                    ptr++;
                }
            }
            return (result);
        }
</pre>

<img src="https://asecuritysite.com/content/baud.jpg"/>


<h2>Random Number Generator</h2>

The Linear Congruential Random Number Generator is a popular method of creating random numbers. It is linear congruential as the values are related to each other in a linear way, modulo m. It uses the sequence generator of:

Xi =(a×Xi−1+c) (mod m)

and where X0 is the initial seed value of the series. Enter some values and the program should generate 200 random values:

Implement the following code:

<pre>
import math

def gen_linear(a, seed,c, m):
	x=seed
	res=""
	for i in range(0,200):
                val = (a * x + c) % m
                res += str(val) + " "
                x = val;
	return (res)
a=21
X0=35
c=31
m=100  
res=gen_linear(a,X0,c,m)
print res
</pre>

<p>Questions:</p>

1. If we use a=21, seed=35, c=31, and m=100, prove that the generated numbers are:

66 17 88 79 90 21 72 43 34 45 76 27 98 89  0 31 82 53 44 55 86 
37  8 99 10 41 92 63 54 65 96 47 18 9 20 51 2 73 64 75 6 57 28 
19 30 61 12 83 74 85 16 67 38 29 40 71 22 93 84 95 26 77 48 39 
50 81 32 3 94 5 36 87 58 49 60 91 42 13 4 15 46 97 68 59 70 1 
52 23 14 25 56 7 78 69 80 11 62 33 24 35

2. If we change the a value to 22, what do you observe from the random values generated?

3. If a developer uses this method to generate encryption keys, what what you expect to happen when the random numbers are generated?
<h2>Prime Numbers</h2>

A prime sieve creates all the prime numbers up to a given limit. It progressively removes composite numbers until it only has prime numbers left, and it is the most efficient way to generate a range of prime numbers. Implement the following code:

<pre>
import sys

test=1000

if (len(sys.argv)>1):
	test=int(sys.argv[1])

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
 
print sieve_for_primes_to(test)
</pre>

Questions:

1. What are the last three prime numbers between 1 and 1,000?

2. What are the last three prime numbers between 1 and 10,000?
