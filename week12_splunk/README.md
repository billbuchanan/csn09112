<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Splunk

## Objectives
The key objectives of this unit are to:

* Understand how to perform a search with SPL (Search Processing Language) in Splunk.
* Understand how to perform key searches within a data set.

## Content
The core content is here:

* YouTube presentation: [here](https://youtu.be/bOQmd6B8jGo).
* Slides: [here](https://asecuritysite.com/public/ch12_splunk.pdf).
* Tutorial: [here](https://asecuritysite.com/public/splunk01.pdf)[here](https://asecuritysite.com/public/splunk02.pdf).
* Access Splunk [here](https://asecuritysite.com:8000/). Contact support@asecuritysite.com for a login.
* Test [here](https://asecuritysite.com/tests/tests?sortby=siem).

## Outline

In this case, we will analyse the Buttercup dataset, and which involves the sale of on-line games. The structure of the site is as follows:

![Buttercup](https://asecuritysite.com/public/sp10.png)

Web server logs can provide a whole lots of security information, along with business information. If we look at a standard Apache Web log we can see the information that we can mine from the log (access.log):
```
209.160.24.63 - - [19/Apr/2014:18:22:16] "GET /product.screen?productId=WC-SH-A02&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 3878 "http://www.google.com" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 349
209.160.24.63 - - [19/Apr/2014:18:22:16] "GET /oldlink?itemId=EST-6&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 1748 "http://www.buttercupgames.com/oldlink?itemId=EST-6" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 731
209.160.24.63 - - [19/Apr/2014:18:22:17] "GET /product.screen?productId=BS-AG-G09&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 2550 "http://www.buttercupgames.com/product.screen?productId=BS-AG-G09" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 422
209.160.24.63 - - [19/Apr/2014:18:22:19] "POST /category.screen?categoryId=STRATEGY&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 407 "http://www.buttercupgames.com/cart.do?action=remove&itemId=EST-7&productId=PZ-SG-G05" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 211
```

We can see that we can now timeline the transactions on a site and the links accessed. Also we have the information the HTTP response code, where at 200 defines that the HTTP request was successful, and a 404 means that the page was not found. Let’s now search for the GET HTTP request and view the number of transactions. The following figure shows the result, where for this example, we get 24,866 results:

![Image](https://asecuritysite.com/public/sp01.png)

If we use a smart mode, as shown in the following, we can automatically parse the log in order to mine the information in the fields from the GET request:

![Image](https://asecuritysite.com/public/sp02.png)

This view now allows us to mine the data associated with each of the fields. For example we can mine for the Client IP address to see the highest number of accesses:

```
Top 10 Values     Count     %
87.194.216.51     651     2.618%
211.166.11.101    473     1.902%
128.241.220.82    364     1.464%
194.215.205.19    316     1.271%
188.138.40.166    276     1.11%
109.169.32.135    257     1.034%
107.3.146.207     215     0.865%
216.221.226.11    195     0.784%
74.208.173.14     190     0.764%
74.53.23.135      189     0.76%
```

So straight-away we can find out the main IP addresses who have been accessing our sites. Next we can have a look at all the HTTP response codes so see how our site is performing:

```
Values     Count     %
200  20,890     84.01%
408     591     2.377%
500     588     2.365%
400     573     2.304%
406     565     2.272%
404     553     2.224%
503     527     2.119%
505     391     1.572%
403     188     0.756%
```

So we can see that most of the responses give us a 200 (OK) response, but there are other codes which could identify either a problem with the Web site, or security events. A 408, for example, is a request timeout error, which perhaps shows a problem on the Web site for some transactions. Also a 404 error is a file not found response, which either means that there’s a missing file on the site, or someone could be fishing for files. Our search can now become:

```
get status=404
```
![Image](https://asecuritysite.com/public/sp03.png)


So again we can mine for the Client IP address to see the hosts that are generating most of the requests for files not found:

```
Top 10 Values     Count     %
87.194.216.51     18     3.255%
211.166.11.101    12     2.17%
88.12.32.208       9     1.627%
124.160.192.241    8     1.447%
128.241.220.82     8     1.447%
91.205.189.15      8     1.447%
109.169.32.135     7     1.266%
117.21.246.164     7     1.266%
148.107.2.20       7     1.266%
175.44.1.122       7     1.266%
```

So there was thus 18 requests from 87.194.216.51 for file not found. So we can then search for:

```
get status=404 clientip="87.194.216.51"
```

This gives us 18 events of:

```
87.194.216.51 - - [17/Mar/2014:18:21:45] "GET /search.do?items=2112&JSESSIONID=SD2SL1FF10ADFF46115 HTTP 1.1" 404 1585 "http://www.buttercupgames.com/cart.do?action=view&itemId=EST-16" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.28) Gecko/20120306 YFF3 Firefox/3.6.28 ( .NET CLR 3.5.30729; .NET4.0C)" 920

87.194.216.51 - - [17/Mar/2014:17:52:09] "GET /productscreen.html?t=ou812&JSESSIONID=SD2SL3FF1ADFF46010 HTTP 1.1" 404 2391 "http://www.buttercupgames.com/product.screen?productId=SF-BVS-G01" "Opera/9.20 (Windows NT 6.0; U; en)" 575

87.194.216.51 - - [17/Mar/2014:10:30:39] "GET show.do?productId=SF-BVS-01&JSESSIONID=SD2SL7FF10ADFF43983 HTTP 1.1" 404 1870 "http://www.buttercupgames.com/cart.do?action=view&itemId=EST-12" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0;BOIE9;ENUS)" 908

87.194.216.51 - - [17/Mar/2014:00:11:08] "GET /hidden/anna_nicole.html?JSESSIONID=SD4SL6FF7ADFF40941 HTTP 1.1" 404 2262 "http://www.buttercupgames.com/oldlink?itemId=EST-19" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152;.NET CLR 3.5.30729; InfoPath.1; .NET4.0C; .NET4.0E; MS-RTC LM 8)" 612

87.194.216.51 - - [16/Mar/2014:11:10:31] "GET /stuff/logo.ico?JSESSIONID=SD10SL4FF8ADFF37373 HTTP 1.1" 404 3166 "http://www.buttercupgames.com/oldlink?itemId=EST-6" "Googlebot/2.1 (http://www.googlebot.com/bot.html)" 932

87.194.216.51 - - [16/Mar/2014:05:41:17] "GET /stuff/logo.ico?JSESSIONID=SD6SL4FF7ADFF36073 HTTP 1.1" 404 310 "http://www.buttercupgames.com/product.screen?productId=SF-BVS-G01" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 778

87.194.216.51 - - [16/Mar/2014:04:33:26] "GET /passwords.pdf?JSESSIONID=SD6SL2FF1ADFF35804 HTTP 1.1" 404 1001 "http://www.buttercupgames.com/category.screen?categoryId=NULL" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5" 497
```

One thing we can notice is that there is an access to passwords.pdf, which looks suspicious, so let’s mine for that:

```
passwords.pdf
```

This can then be used to determine the range of IP addresses that searched for this file, and gives:

```
178.162.239.192    3     4.412%
87.194.216.51      3     4.412%
110.159.208.78     2     2.941%
118.142.68.222     2     2.941%
128.241.220.82     2     2.941%
198.35.1.10        2     2.941%
210.76.124.106     2     2.941%
211.166.11.101     2     2.941%
221.204.246.72     2     2.941%
69.72.161.186      2     2.941%
```

The great thing about log analysis is that we can also use the same logs for security to analyse business activity. The first thing can be observed is that the action used to purchase goods on the Web site is “purchase”, so let’s search for purchased items:

```
sourcetype=access_* status=200 action=purchase | top categoryId
```

This then gives us a table of the successful purchases (which are uses that return a 200 code):

```
categoryId     count  percent
STRATEGY      806     30.495649
ARCADE        493     18.653046
TEE           367     13.885736
ACCESSORIES   348     13.166856
SIMULATION    246     9.307605
SHOOTER       245     9.269769
SPORTS        138     5.221339
```

Next we can find the number of unsuccessful purchases with:

```
sourcetype=access_* status!=200 action=purchase | top categoryId
```

to give:
```
categoryId   count     percent
STRATEGY     79     23.442136
NULL         71     21.068249
ARCADE       44     13.056380
ACCESSORIES  39     11.572700
TEE          37     10.979228
SHOOTER      30     8.902077
SIMULATION   27     8.011869
SPORTS       10     2.967359
``` 

and even visualise the sales with:

![image](https://asecuritysite.com/public/sp04.png)

Now our marketing department want to know which is the most popular Web browser, so we can use a search of:

```
get
| top limit=20 useragent
```

and to give [here]:
```
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.28) Gecko/20120306 YFF3 Firefox/3.6.28 ( .NET CLR 3.5.30729; .NET4.0C)     5282     21.241856%
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5     2383     9.583367
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; InfoPath.1; MS-RTC LM 8)     2130     8.565913
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5     2021     8.127564
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; MS-RTC LM 8; InfoPath.2)     1898     7.632912
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; BOIE9;ENUS)     1770     7.118153
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3     1121     4.508164
Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5     1064     4.278935
Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3     1000     4.021556
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5     992     3.989383
Opera/9.01 (Windows NT 5.1; U; en)     430     1.729269
```
    

We can then see from this that Firefox running on Windows is our most popular browser, followed by Chrome running on Mac OS (AppheWebkit) and then Microsoft Internet Explorer Version 7. This type of information is obviously important for the design of a site, as it focuses the development on the browsers that will typically be used to access the site. Then, if we classify for Safari, Chrome and Mozilla we can chart with [here]:

```
sourcetype=access_* | chart  count(eval(searchmatch("Safari")))  AS Safari,
count(eval(searchmatch("Chrome")))  AS Chrome, count(eval(searchmatch("Mozilla"))) AS Mozilla
```

and then we can chart types with:

![image](https://asecuritysite.com/public/sp05.png)

When we view a URI, we see is that the parameters used, and which can be mined:

```
182.236.164.11 – – [18/Mar/2014:18:20:54] “POST /cart.do?action=purchase&itemId=EST-6&JSESSIONID=SD6SL8FF10ADFF53101 HTTP 1.1″ 200 1803 “http://www.buttercupgames.com/cart.do?action=addtocart&itemId=EST-6&categoryId=ARCADE&productId=MB-AG-G07” “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5” 524

182.236.164.11 – – [18/Mar/2014:18:20:53] “POST /cart.do?action=addtocart&itemId=EST-6&productId=MB-AG-G07&JSESSIONID=SD6SL8FF10ADFF53101 HTTP 1.1″ 200 533 “http://www.buttercupgames.com/product.screen?productId=MB-AG-G07” “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5” 470
```

For example we have action, productID and itemID as parameters which are set, and passed back to the server. Thus we can mine these for the action undertaken, and the products. So we can search now for ProductIDs with:

post action=purchase action=purchase productid

To give [here]:
```
productId     count     percent
WC-SH-G04     275     9.404925
SC-MG-G10     273     9.336525
DB-SG-G01     266     9.097127
MB-AG-T01     231     7.900137
DC-SG-G02     226     7.729138
MB-AG-G07     223     7.626539
FS-SG-G03     221     7.558140
WC-SH-A02     205     7.010944
WC-SH-A01     182     6.224350
WC-SH-T02     173     5.916553
PZ-SG-G05     172     5.882353
FI-AG-G08     163     5.574555
BS-AG-G09     151     5.164159
CU-PG-G06     148     5.061560
SF-BVS-G01     15     0.51
```

We can also discover the mappings of the CategoryID to Product IDs, such as with [here](https://asecuritysite.com:8000/en-GB/app/search/search?q=search%20get%20cart.do%20productId%3D%22WC-SH-G04%22%20%7C%20top%20categoryId&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=&display.page.search.tab=statistics&display.general.type=statistics&sid=1593552643.128):
```
get cart.do productId="WC-SH-G04" | top categoryId

```
![image](https://asecuritysite.com/public/sp06.png)

We can now see that WC-SH-G04 is a SHOOTER game [here](https://asecuritysite.com:8000/en-GB/app/search/search?q=search%20get%20cart.do%20categoryId%3D%22STRATEGY%22%20%7C%20top%20productId&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=&display.page.search.tab=statistics&display.general.type=statistics&sid=1593552806.130):
```
get cart.do categoryId="STRATEGY" | top productId
```
![image](https://asecuritysite.com/public/sp06.png)

We can see that DB-SG-G01, DC-SG-G02, FS-SG-G03 and PZ-SG-G05 are STRATEGY games.


