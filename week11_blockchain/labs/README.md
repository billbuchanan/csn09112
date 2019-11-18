<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

## Introduction
This provides an outline of cryptocurrencies and blockchain:

* Lab (PDF): [here](https://asecuritysite.com/public/blockchain_lab.pdf)

## Genesis Block Code
Here is the custom.json:
<pre>
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip150Block": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "20000000",
    "gasLimit": "0x3d0900",
    "alloc": {
        "228041751ddb7365cc4bc75c4985d14d5db2432f": { "balance": "30000000" },
        "cdfc92d1b5dd1c9ee1c9e2368abc86a193ae35a5": { "balance": "40000000" },
        "c9c425ae15a0e66500ecf5b7a1c10c6ed35600b9": { "balance": "0x400000000000000" }

    }
}
</pre>

## Bitcoin API code
Here is the bit.py file. This is defined in Python 3.7. For Python 2.7, you can remove the brackets in the print statements):
<pre>
import httplib2

resp, content = httplib2.Http().request("https://blockchain.info/q/latesthash")
print ("Latest hash: ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/bcperblock")
print ("Block reward per block: ",int(content)/100000000.0)

resp, content = httplib2.Http().request("https://blockchain.info/q/getblockcount")
print ("Longest block: ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/getdifficulty")
print ("Difficulty: ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/probability")
print ("Mining probability: ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/interval")
print "Average time between blocks (seconds): ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/eta")
print ("Time to next block (seconds): ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/marketcap")
print ("Market capitalisation (Million USD): ",float(content)/1000000)


resp, content = httplib2.Http().request("https://blockchain.info/q/24hrprice")
print ("24hr price (USD): ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/24hrtransactioncount")
print ("24hr transactions: ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/hashrate")
print ("Hash rate: ",content)

resp, content = httplib2.Http().request("https://blockchain.info/q/addressbalance/1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to?confirmations=1")
print ("Account balance for 1Gb...4to (BTC): ",int(content)/100000000)

resp, content = httplib2.Http().request("https://blockchain.info/q/getreceivedbyaddress/1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to?confirmations=1")
print ("Received for 1Gb...4to (BTC): ",int(content)/100000000)
</pre>
