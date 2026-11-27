<img width="1086" height="214" alt="image" src="https://github.com/user-attachments/assets/24af435f-a598-43a0-819c-d92cae38b1b0" />


## Introduction
This provides an outline of cryptocurrencies and blockchain:

* Lab (PDF): [here](https://asecuritysite.com/public/blockchain_lab.pdf)

## Part A

**Using blockchain.info, find the details of the genesis block:**

Date created:

Reward:

Number of transactions:

Size of block:

Which account received the mining reward for the genesis block (last four digits):

How many USD does the original miner have in the account they used for the first genesis record:

When did the genesis block creator stop trading?


**L1.2	Using blockchain.info, determine the following:**

Total bitcoins in circulation:

Most recent hash block (last four hex digits):

Block reward per block:

Difficulty:

Average time between blocks:

Market capitalisation (USD):

24 hr price (USD):

24hr transactions (USD):

Hash rate:

Last successful miner:

Maximum block size:

Balance for 1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to:


**L1.3 Download and created the Python file defined on this page:**

https://asecuritysite.com/encryption/bit

Now run the Python file, and compare the results in L.1.2.

Total bitcoins in circulation:

Most recent hash block (last four hex digits):

Block reward per block:

Difficulty:

Average time between blocks:

Market capitalisation (USD):

24 hr price (USD):

24hr transactions (USD):

Hash rate:



## B	Ethereum
## Setting up your Ethereum wallet on Sepolia
The Sepolia network allows a user to test an Ethereum application, and using free Ether. Initially setup your MetaMask wallet. A document to outline how you set this up is [here](https://github.com/billbuchanan/appliedcrypto/blob/main/unit08_blockchain/lab/Metamask.pdf). Once you have set it up, answer the following:

* What is your public ID (just define the first four hex values)?
* Find out someone else's public ID, and send them 0.001 Ether. If you are doing the lab on your own, send it to Bill (ID: 0xbB15B38e4ef6aF154b89A2E57E03Cd5cbD752233).
* Can you see the transaction on the Ethereum network? An example of a wallet is [here](https://sepolia.etherscan.io/address/0xbb15b38e4ef6af154b89a2e57e03cd5cbd752233).
* Can you see your transaction on the Ethereum network for the person you send it to?
* What was the transaction fee for the transfer? If you were using the main Ethereum network, how much would the transaction cost in Dollars?
* Ask someone to send you 0.001 Ether. Did you receive it? If you are doing the lab on your own, ask your lab tutor to send you 0.001 Ether.

## Creating a Smart Contract in Ethereum
So, let’s write a bit of code that does some simple maths. In the following we will implement sqrt(), sqr(), mul(), sub(), and add(). First, we open up https://remix.ethereum.org/. and enter the following Solidy contract:

```solidity
pragma solidity ^0.8.0;
contract mymath {function sqrt(uint x) public view returns (uint y) {
    uint z = (x + 1) / 2;
    y = x;
    while (z < y) {
        y = z;
        z = (x / z + z) / 2;
    }
}
function sqr(uint a) public view returns (uint) {
    uint c = a * a;
    return c;
  }
function mul(uint a, uint b) public view returns (uint) {
    uint c = a * b;
    return c;
  }
function sub(uint a, uint b) public view returns (uint) {
    return a - b;
  }
function add(uint a, uint b) public view returns (uint) {
    uint c = a + b;
    return c;
}}
 ``` 

In this case, the "public" part makes sure we can see the output of the function, and the "view" part allows it to be stateless (and where we just have to receiver the value without the smart contact remember the state). On Ethereum we normally use the Solidity language to create a smart contract and then compile it into the byte code required for the ledger. First, can we start by entering the Solidity code into Remix [<a href="https://remix.ethereum.org/" target="_blank">here</a>]:

<img width="2264" height="1228" alt="image" src="https://github.com/user-attachments/assets/22efa8ad-64b2-4078-a63d-cce1bafda22f" />


Once entered, we can then compile it with the Solidity compiler. It is important to take a note of the compiler version at this stage, as we will need this later:

<img width="2398" height="1222" alt="image" src="https://github.com/user-attachments/assets/24290b75-69d3-4dbc-871d-f3c94dde7606" />

   
Once compiled, we can then deploy the smart contract to a test network (Sepolia). For this, we need to connect our Metamask wallet:
   
<img width="1273" height="572" alt="image" src="https://github.com/user-attachments/assets/6a61c6a8-6d72-4725-8788-19c159401b9f" />


Once it has been deployed, we can see our wallet identifies the deployed contract:
    
 <img width="2426" height="1204" alt="image" src="https://github.com/user-attachments/assets/24461552-c7a4-453b-b31c-9766c38d3c4c" />


And clicking through gives us the address of the contract, and then viewing it on the explorer, we can see the transaction:
    
 <img width="2284" height="846" alt="image" src="https://github.com/user-attachments/assets/959a9393-b5cd-48c2-9f4b-d1bf49a5397e" />


The address in the screenshot above is “0x0895..”, so you can click on your own address and view the smart contract in Etherscan. 

In another example: 

![image](https://user-images.githubusercontent.com/44439128/205040755-0796dba5-c8ab-4f6e-ad74-5e023e32d4fb.png)

The address of the contract is "0x3a40..", so you can visit it from: [here](https://sepolia.etherscan.io/address/0x3a407068a13bfef0db1e319c364c153391b158cf). We now need to verify and publish the contact, with click on “Verify and Publish”:
    
<img width="2402" height="1058" alt="image" src="https://github.com/user-attachments/assets/a7c73ce4-394b-4b78-bd0a-1da98213f9b3" />

After this, we can define the Compiler Version and the licence
    
<img width="2046" height="1220" alt="image" src="https://github.com/user-attachments/assets/e67daa6a-f536-4cbd-851e-8081f7ed717d" />

We then need to add your code for it to be checked:
    
 <img width="2176" height="1186" alt="image" src="https://github.com/user-attachments/assets/ad9dca07-3a0f-4006-959f-a869bb0074eb" />

 It takes around 30 seconds, but, eventually, we should have our code accepted:
    
 <img width="2134" height="1224" alt="image" src="https://github.com/user-attachments/assets/d4dedbe1-7ed4-4465-b0c2-4e4768635d65" />

We now have the contract published to the Sepolia test network:
    
<img width="2202" height="1146" alt="image" src="https://github.com/user-attachments/assets/29b3d2be-ca5f-4a7b-940e-2628b204ecaf" />

Next, by selecting the Contract tab, we can view the read parameters. The exposed functions are add(), mul(), sqr(), sqrt() and sub():
    
<img width="2156" height="1074" alt="image" src="https://github.com/user-attachments/assets/df355108-ad9a-45bd-924a-5f9f890bb952" />

To test, we can just enter the variables for a given function, and get a result:
    
<img width="2168" height="1030" alt="image" src="https://github.com/user-attachments/assets/23f60bfd-4fb3-48d9-ab66-6dd077c69a6e" />
 
Note: You can get Ether for our wallet [here](https://faucet.metamask.io/)

## Creating ERC-20 tokens
Within the Ethereum blockchain, we can record transactions and run smart contracts. These things allow us to run DApps (decentralized applications) and which can support the running of the infrastructure in return for some payment (Ether). A DApp can also create tokens for new currencies, shares in a company or to prove the ownership of an asset. ERC-20 is a standard format for a Fungible Token and which can support the sharing, transfer and storage of tokens. These tokens are supported by the whole of the Ethereum infrastructure and can be easily traded. They support a number of mandatory functions:


* totalSupply. This function is the total number of ERC-20 tokens that have been created.
* balanceOf. This function identifies the number of tokens that a given address has in its account.
* transfer. This function supports the transfer of tokens to a defined user address.
* transferFrom. This function supports a user to transfer tokens to another user.
* approve. This function checks that a transaction is valid, based on the supply of token.
* allowance. This function checks if a user has enough funds in their account for a transaction.
 
There are also a number of options:

* Token Name. This is the name that the token will be defined as.
* Symbol. This is the symbol that the token will use.
* Decimal. This is the number of decimal places to be used for any transactions.

Now you can create your own token. If you are Bob Smith, then call your token "BobSmithToken", and your currency will be "BobSmith". 

So, let's create a token named "ENUToken" (change the name to your name), and use the tutorial sample from [here](https://github.com/bitfwdcommunity/Issue-your-own-ERC20-token/blob/master/contracts/erc20_tutorial.sol). First, we open up [https://remix.ethereum.org/](https://remix.ethereum.org/), and enter the following Solidy contract:


```solidity
pragma solidity ^0.4.24;

// ----------------------------------------------------------------------------
// 'ENU Token' token contract
//
// Deployed to : 0xbB15B38e4ef6aF154b89A2E57E03Cd5cbD752233
// Symbol      : ENUToken
// Name        : ENU Token
// Total supply: 100000000
// Decimals    : 18

// Based on https://github.com/bitfwdcommunity/Issue-your-own-ERC20-token/tree/master/contracts


// ----------------------------------------------------------------------------
// Safe maths
// ----------------------------------------------------------------------------
contract SafeMath {
    function safeAdd(uint a, uint b) public pure returns (uint c) {
        c = a + b;
        require(c >= a);
    }
    function safeSub(uint a, uint b) public pure returns (uint c) {
        require(b <= a);
        c = a - b;
    }
    function safeMul(uint a, uint b) public pure returns (uint c) {
        c = a * b;
        require(a == 0 || c / a == b);
    }
    function safeDiv(uint a, uint b) public pure returns (uint c) {
        require(b > 0);
        c = a / b;
    }
}


// ----------------------------------------------------------------------------
// ERC Token Standard #20 Interface
// https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
// ----------------------------------------------------------------------------
contract ERC20Interface {
    function totalSupply() public constant returns (uint);
    function balanceOf(address tokenOwner) public constant returns (uint balance);
    function allowance(address tokenOwner, address spender) public constant returns (uint remaining);
    function transfer(address to, uint tokens) public returns (bool success);
    function approve(address spender, uint tokens) public returns (bool success);
    function transferFrom(address from, address to, uint tokens) public returns (bool success);

    event Transfer(address indexed from, address indexed to, uint tokens);
    event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
}


// ----------------------------------------------------------------------------
// Contract function to receive approval and execute function in one call
//
// Borrowed from MiniMeToken
// ----------------------------------------------------------------------------
contract ApproveAndCallFallBack {
    function receiveApproval(address from, uint256 tokens, address token, bytes data) public;
}


// ----------------------------------------------------------------------------
// Owned contract
// ----------------------------------------------------------------------------
contract Owned {
    address public owner;
    address public newOwner;

    event OwnershipTransferred(address indexed _from, address indexed _to);

    constructor() public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function transferOwnership(address _newOwner) public onlyOwner {
        newOwner = _newOwner;
    }
    function acceptOwnership() public {
        require(msg.sender == newOwner);
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
        newOwner = address(0);
    }
}


// ----------------------------------------------------------------------------
// ERC20 Token, with the addition of symbol, name and decimals and assisted
// token transfers
// ----------------------------------------------------------------------------
contract BillToken is ERC20Interface, Owned, SafeMath {
    string public symbol;
    string public  name;
    uint8 public decimals;
    uint public _totalSupply;

    mapping(address => uint) balances;
    mapping(address => mapping(address => uint)) allowed;


    // ------------------------------------------------------------------------
    // Constructor
    // ------------------------------------------------------------------------
    constructor() public {
        symbol = "ENUToken";
        name = "ENU Token";
        decimals = 18;
        _totalSupply = 100000000000000000000000000;
        balances[0xbB15B38e4ef6aF154b89A2E57E03Cd5cbD752233] = _totalSupply;
        emit Transfer(address(0), 0xbB15B38e4ef6aF154b89A2E57E03Cd5cbD752233, _totalSupply);
    }


    // ------------------------------------------------------------------------
    // Total supply
    // ------------------------------------------------------------------------
    function totalSupply() public constant returns (uint) {
        return _totalSupply  - balances[address(0)];
    }


    // ------------------------------------------------------------------------
    // Get the token balance for account tokenOwner
    // ------------------------------------------------------------------------
    function balanceOf(address tokenOwner) public constant returns (uint balance) {
        return balances[tokenOwner];
    }


    // ------------------------------------------------------------------------
    // Transfer the balance from token owner's account to to account
    // - Owner's account must have sufficient balance to transfer
    // - 0 value transfers are allowed
    // ------------------------------------------------------------------------
    function transfer(address to, uint tokens) public returns (bool success) {
        balances[msg.sender] = safeSub(balances[msg.sender], tokens);
        balances[to] = safeAdd(balances[to], tokens);
        emit Transfer(msg.sender, to, tokens);
        return true;
    }


    // ------------------------------------------------------------------------
    // Token owner can approve for spender to transferFrom(...) tokens
    // from the token owner's account
    //
    // https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
    // recommends that there are no checks for the approval double-spend attack
    // as this should be implemented in user interfaces 
    // ------------------------------------------------------------------------
    function approve(address spender, uint tokens) public returns (bool success) {
        allowed[msg.sender][spender] = tokens;
        emit Approval(msg.sender, spender, tokens);
        return true;
    }


    // ------------------------------------------------------------------------
    // Transfer tokens from the from account to the to account
    // 
    // The calling account must already have sufficient tokens approve(...)-d
    // for spending from the from account and
    // - From account must have sufficient balance to transfer
    // - Spender must have sufficient allowance to transfer
    // - 0 value transfers are allowed
    // ------------------------------------------------------------------------
    function transferFrom(address from, address to, uint tokens) public returns (bool success) {
        balances[from] = safeSub(balances[from], tokens);
        allowed[from][msg.sender] = safeSub(allowed[from][msg.sender], tokens);
        balances[to] = safeAdd(balances[to], tokens);
        emit Transfer(from, to, tokens);
        return true;
    }


    // ------------------------------------------------------------------------
    // Returns the amount of tokens approved by the owner that can be
    // transferred to the spender's account
    // ------------------------------------------------------------------------
    function allowance(address tokenOwner, address spender) public constant returns (uint remaining) {
        return allowed[tokenOwner][spender];
    }


    // ------------------------------------------------------------------------
    // Token owner can approve for spender to transferFrom(...) tokens
    // from the token owner's account. The spender contract function
    // receiveApproval(...) is then executed
    // ------------------------------------------------------------------------
    function approveAndCall(address spender, uint tokens, bytes data) public returns (bool success) {
        allowed[msg.sender][spender] = tokens;
        emit Approval(msg.sender, spender, tokens);
        ApproveAndCallFallBack(spender).receiveApproval(msg.sender, tokens, this, data);
        return true;
    }


    // ------------------------------------------------------------------------
    // Don't accept ETH
    // ------------------------------------------------------------------------
    function () public payable {
        revert();
    }


    // ------------------------------------------------------------------------
    // Owner can transfer out any accidentally sent ERC20 tokens
    // ------------------------------------------------------------------------
    function transferAnyERC20Token(address tokenAddress, uint tokens) public onlyOwner returns (bool success) {
        return ERC20Interface(tokenAddress).transfer(owner, tokens);
    }
}
```

When you create your own contract, make sure you change the public constructor() with: the **symbol**, the **name**, and the **wallet ID**. You are the owner of the token, so you need to enter the public ID of your wallet for two hex values given next:

```solidity
    constructor() public {
    symbol = "ENUToken";
    name = "ENU Token";
    decimals = 18;
    _totalSupply = 100000000000000000000000000;
    balances[0xbB15B38e4ef6aF154b89A2E57E03Cd5cbD752233] = _totalSupply;
    emit Transfer(address(0), 0xbB15B38e4ef6aF154b89A2E57E03Cd5cbD752233, _totalSupply);
    }
```

The wallet ID is the public ID of your wallet in Metamask. Now we compile:

<img width="2262" height="1144" alt="image" src="https://github.com/user-attachments/assets/61d35c1f-afcc-49e0-8725-ec9d2fcdd2b7" />


Next, we will deploy to the Sepolia test network:

<img width="2408" height="1212" alt="image" src="https://github.com/user-attachments/assets/2a871025-bc28-47de-bc46-9394e6fd4b12" />

After this, our contract will be shown as being pending deployment:

<img width="2426" height="1188" alt="image" src="https://github.com/user-attachments/assets/9775d95d-ade5-47e6-b8c7-b59ae80e769c" />

It will take 10–15 minutes to deploy, but it can be sped up by increasing the gas limit:

<img width="636" height="1060" alt="image" src="https://github.com/user-attachments/assets/c16ac7fb-ba57-4545-ace6-ceda78db003b" />

Once deployed, we can view the contract details:

<img width="2408" height="1190" alt="image" src="https://github.com/user-attachments/assets/c32bcefa-02d5-4649-8f45-8d36aecce264" />

And can then view the transaction for the contract: 
<!-- [<a href="https://ropsten.etherscan.io/tx/0x70604b7c25c12eea5210c75afaa89879f383dc94b894d570f06925d0d95b7fdb" target="_blank">here</a>] -->

<img width="1455" height="684" alt="image" src="https://github.com/user-attachments/assets/1e61c43f-0c5c-46e1-86ed-5f7ffb44ebee" />


And then view the contact: 
<!-- [here](https://ropsten.etherscan.io/address/0x7db2f938e1037a13dde315634a71a91625542a52")] -->

<img width="2236" height="1196" alt="image" src="https://github.com/user-attachments/assets/3bb53b56-9d2b-4334-8cd1-1f12b7190761" />

Next, we select the Contract tab:
    

<img width="2156" height="1210" alt="image" src="https://github.com/user-attachments/assets/7c3fe9c8-f3a3-4aee-a134-31e00d90f8dc" />


And then select "Verify and Publish" and enter the details of the compiler version (v0.4.26):

<img width="1868" height="1070" alt="image" src="https://github.com/user-attachments/assets/4b860880-d2ef-4086-9555-ac4987fc3878" />


We then need to copy-and-paste the contract code into the Source Code text box:

<img width="2174" height="1192" alt="image" src="https://github.com/user-attachments/assets/8304876e-03d4-41fc-bbd9-6f7b58d0548d" />


After less than 45 seconds, the contract will be approved:
    
<img width="2094" height="1210" alt="image" src="https://github.com/user-attachments/assets/245effa9-9a14-4cca-a98b-89e4726fbd94" />

When the contract is run, there is a constructor to transfer the tokens to the wallet we have defined (and who will be the owner of the token). We can now go back to the wallet which is specified, to see if the tokens have been transferred:

<img width="2214" height="1146" alt="image" src="https://github.com/user-attachments/assets/7a88b09d-526e-4f64-8375-99170fbd8366" />


Next, we can transfer the tokens into our wallet, by defining the contract address:

<img width="2220" height="1152" alt="image" src="https://github.com/user-attachments/assets/c5c52ba7-f294-4e54-894f-560bccff9864" />


We will now have our new tokens in the wallet:

<img width="2258" height="1150" alt="image" src="https://github.com/user-attachments/assets/92adf618-6194-454d-9c95-70cd7540f5f9" />

And with:

<img width="2164" height="1126" alt="image" src="https://github.com/user-attachments/assets/69dce86a-d0a6-4b0c-aea8-a547ddaab2de" />


We can now transfer the cryptocurrency to another wallet:

<img width="1455" height="644" alt="image" src="https://github.com/user-attachments/assets/2d484a29-dec8-4b1b-8cc0-8ade00153705" />


We can view the ENUToken:
<!-- [here](https://ropsten.etherscan.io/token/0x7db2f938e1037a13dde315634a71a91625542a52)] -->

<img width="2684" height="952" alt="image" src="https://github.com/user-attachments/assets/8e4a4366-c654-4ce7-98ae-2fb0eab19ba7" />

Now answer the following:

* Do you see the tokens in your wallet?
* Now send 0.1 of your token to someone else's wallet. If you want, you can send to your tutor's wallet. Bill's wallet is 0xbb15b38e4ef6af154b89a2e57e03cd5cbd752233
* Did they receive the token?
