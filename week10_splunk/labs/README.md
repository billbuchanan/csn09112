<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Splunk Tutorial

## Question 1.

If you want to see the answers, click [here](https://asecuritysite.com/cyberdata/ch15_02).

Using Splunk at [link](https://asecuritysite.com:8443) determine the following [PDF](https://asecuritysite.com/public/splunk01.pdf). You will be allocated a login.

* What is the start date of the log? 
* How many log events are in *mailsv/secure.log  (Hint: Click the Search tab, and click on Data Summary, and select Data Sources)? 
* How many log events are in *www1/access.log? 
* How many log events are in *www1/secure.log? How many log events are in *www2/access.log? 
* What is the first username in the security log that gave an incorrect password? 
* What is the first IP address in the security log that gave an incorrect password? 
* How many accesses were accessed by a "Chrome" browser and a "GET" method request? 
* How many accesses were accessed by a "Chrome" browser or a "GET" method request? 
* How many accesses were accessed by a "Chrome" browser and a "POST" method request? 
* How many accesses were access by a "Chrome" browser or a "POST" method request? 
* When was the peak accesses by a "Chrome" browser or a "POST" method request?
* How many accesses are there from a Safari browser? 
* How many accesses are there from a Chrome browser? 
* How many accesses are there from a Mozilla browser? 
* On what day is there most activity in the secure logs? For the access.log from www1, which is the most popular HTTP response value? For the access.log from www1, which is the second most popular HTTP response value? 
* For the access.log from www1, which is the most popular IP address for accesses? 
* For the access.log from www1, which is the second most popular IP address for accesses? Refer to the Splunk analysis. For the access.log from www1, there is a parameter named action, which is the most popular value for the action parameter? 
* Refer to the Splunk analysis. For the access.log from www1, there is a parameter named action, which is the second most popular value for the action parameter? For the access.log from www1, estimate the number of iPad accesses? 
* For the access.log from www1, what is the top refer domain: Which is the first time for a refer from Google?
* Which is the IP address of the client which is first referred from google.com?
* Are there any successful accesses to signals.zip? 
* Refer to the Splunk analysis for secure*.log. How many failed password attempts were there from 194.8.74.23? 
* Refer to the Splunk analysis for secure*.log. What day of the week had the most failed password attempts from 194.8.74.23? 
* Which day had the most successful purchases? Which day had the fewest purchases? 
* Which day had the most purchases which were not successfully processed? 
* How many STRATEGY games have been successfully purchased? 
* Which file access always produces a 404 return message: anna_nicole.html, productscreen.html, numa.html, cart.do and/or oldlink? 
* How many SIMULATION games have been successfully purchased? How many SHOOTER games have been successfully purchased? 
* How many SHOOTER games have been unsuccessfully purchased? 
* Refer to the Splunk analysis for secure*.log. What day of the week had the least failed password attempts from 194.8.74.23? 
* For an HTTP GET request, which is the most popular return code For an HTTP GET request, which is the 2nd most popular return code How many IP addresses have accessed the "passwords.pdf" file. 
* What is/are the return HTTP status code(s) for these accesses? For an HTTP GET request, which is the 2nd most popular return code?

## Question 2. 
We can use regular expressions to find information. For example, to find the number of accesses from an IP address which starts with “182.”, we can use [here]:
```
get | regex _raw="182\.\d{1,3}\.\d{1,3}\.\d{1,3}"
```

Determine the number of accesses for GET from any address which begins with 182:

## Question 3. 
The security team search for an address that is ending with .22, and do a search with [here]:
```
get | regex _raw="\d{1,3}.\d{1,3}.\d{1,3}.22"
```

But it picks up logs which do not include addresses with .22 at the end. What is the problem with the request, and how would you modify the request:

## Question 4. 
You are told that there’s access to a file which ends in “a.html”. Using a regular expression, such as [here]:
```
get | regex _raw="[a]+\.html"
```
Outline three HTML files which end with the characters ‘a’, or an ‘e’, and have ‘.html’ as an extension:

## Question 5. 
A simple domain name check is [here]:
```
get | regex _raw="[a-zA-Z\.]+\.(com|net|uk)"
```

## Question 6.
If we now try [here]:
```
get | regex _raw="[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|UK)"
```

we will return events with domain names.

Outline which ones have been added:

## Question 7
We can search for email addresses with [here]:

```
get | regex _raw="(?<email>[\w\d\.\-]+\@[\w\d\.]+)""
```
Which email addresses are present:

## Question 8
We can search for times using regular expressions, such as [here]:
```
get | regex _raw="[0-9]{2}\:22\:[0-9]{2}"
```
How many GET requests where there at 22 minutes past the hour:

How many GET requests were made at 14 seconds past the minute:

## Question 9
The incident response team wants a report of unusual HTTP requests. Produce a report of the HTTP response codes, and what they identify. Which ones could be malicious?

* The security team would like a report on the most popular user names that have failed on the security logs. What would you report?
* The company are worried about the sales of some of their games. Which game category has the least amount of sales, and which is the best seller?
* The Web design department have been told that there are missing files on the Web site. Investigate the files/pages that are missing on the site (Hint: 404 codes). What would you report?
* The IT Team are worried about system outages on the Web server. Can you report on possible Web server downtimes (Hint: the 5xx codes often identify server problems)?
* You have been asked to investigate access to the file named passwords.pdf in the Buttercup Games Splunk trace. Investigate any accesses related to it, and outline any possible significant evidence of malicious activity related to these accesses.

What would you report?

# Splunk installation on Windows (Advanced)
On AWS, create a Windows 2022 instance and gain access to it (note, you may need to create an instance with at least 2GB of memory). 

Create a Splunk account, and then install Splunk Enterprise [here](https://www.splunk.com/en_us/download/splunk-enterprise.html).

Once your server is up and running. Now, enter the command line, and stop the server:

```
splunk stop
```

Check that the server is stopped, and restart it with:

```
splunk stop
```

Next add a new user (user01) and with a password of "snowsnow":

```
splunk add user user01  -password snowsnow  -role user -auth Administrator:<password>
```

Now test that the user can log in with the required password. Now download the Buttercup games data source [here](https://asecuritysite.com/buttercup.zip). We can then add data sources to the server (replace the file location with the location on your system):

```
splunk stop
splunk clean eventdata --no-prompt
splunk start
splunk add oneshot c:\buttercup.zip -index main -auth Administrator:<password>
```

Now access your server, and you should be able to access the Buttercup Games data source. We do not have a TLS connection, and will now need to add a certificate to the server. For this, we can use a self-signed certificate [here](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/9.1/secure-splunk-platform-communications-with-transport-layer-security-certificates/how-to-create-and-sign-your-own-tls-certificates).

# Test

Now perform the following test: [here](https://asecuritysite.com/tests/tests?sortby=siem).
