
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
Prime Numbers

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
