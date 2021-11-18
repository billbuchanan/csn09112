<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>


# Step-by-step
A demo is [here](https://www.youtube.com/embed/u7qsIfCXZng)

From the Apps interface, select Splunk Machine Learning (Figure 1).

![Alt text](https://asecuritysite.com/public/splunk_ml01.png)

Figure 1: Splunk Apps


We will now analyse a firewall log for malware. For this select “Predict Numeric Fields”, and then “Create New Experiment”:


![Alt text](https://asecuritysite.com/public/splunk_ml02.png)

Figure 2: Selecting a Predict Categorical Fields experiment


Provide the name of “Firewall” to the experiment title (Figure 3).


![Alt text](https://asecuritysite.com/public/splunk_ml03.png)

Figure 3: Defining a new experiment


Next (Figure 4) entered the search of “| inputlookup firewall_traffic.csv” and select the green search button. It will then populate the data set in the page. Scroll down to the populated dataset and define the following:

```
Number of results in the dataset:

Parameters used in the dataset:

Which field do you think we are likely to train on:

Outline four IP addresses for source addresses:

Outline four IP addresses for destination addresses:
```


![Alt text](https://asecuritysite.com/public/splunk_ml04.png)

Figure 4: Defining the dataset



There are 98,943 results, which is rather large for processing so reduce it to 50,000 (Figure 5).

![Alt text](https://asecuritysite.com/public/splunk_ml05.png)

Figure 5: Filtering to 50,000 records


Next we will use Logistic Regression to predict a value for “used_by_malware” (Figure 6).

```
Which values are possible for the “used_by_malware” parameter?
```



![Alt text](https://asecuritysite.com/public/splunk_ml06.png)

Figure 6: Predicting for “used_by_malware”



Next we shall train against all the other parameters (Figure 7). Finally we are using a 70/30 split, and 70% of training and 30% for testing the model created.


![Alt text](https://asecuritysite.com/public/splunk_ml07.png)

Figure 7: Fields used to predict


Finally, we select the “Fitting Model..” button, and waiting until the model is built. When complete we should see prediction data (Figure 8).

```
Outline the destination IP addresses for two false positives:

Outline the destination IP addresses for two true positives:

Now outline the following:

Precision:
Recall:
Accuracy:
F1:

Outline the confusion matrix:

```




![Alt text](https://asecuritysite.com/public/splunk_ml08.png)

Figure 8: Predictions

![Alt text](https://asecuritysite.com/public/splunk_ml09.png)

Figure 9: Confusion Matric

![Alt text](https://asecuritysite.com/public/splunk_ml10.png)

Figure 10: Confusion Matric



Now click on “Open Search” in the button beside “Fit Model”, and enter the text in italic:


Next press SHIFT-ENTER, and force the “| fit …” to move to the next line:



```
| multireport
[ score precision_recall_fscore_support "used_by_malware" against "predicted(used_by_malware)" average=weighted
| rename fbeta_score as f1
| eval f1 = round(f1, 2)
| eval precision = round(precision, 2)
| eval recall = round(recall, 2)
| fields f1 precision recall ]


[ score accuracy_score "used_by_malware" against "predicted(used_by_malware)"
| eval accuracy = round(accuracy_score, 2)]

| table accuracy f1 precision recall
| stats first(*) as *
```
This should give the output in Figure 11.
Run the result and check the output.


```
What are the results:
```




![Alt text](https://asecuritysite.com/public/splunk_ml13.png)

Figure 11: Update

Finally save the experiment (Figure 12).

![Alt text](https://asecuritysite.com/public/splunk_ml14.png)

Figure 12: Saving experiment


## SVM
We will now use an SVM (Support Vector Machine) model and which is a supervised learning technique. Overall, it is used to create two categories, and will try to allocate each of the training values into one category or the other. Basically, we have points in a multidimensional space, and try to create a clear gap between the categories. New values are then placed within one of the two categories. In this case we will train with SVM, and rerun the model. Now determine the following:

```
Precision:

Recall:

Accuracy:

F1:


```
  


### Additional code
```
| inputlookup firewall_traffic.csv | head 50000 | apply "_exp_draft_0e467230935543b98e7882eebdfce34d"
| table "used_by_malware", "predicted(used_by_malware)", "bytes_received" "bytes_sent" "dest_port" "dst_ip" "has_known_vulnerability" "packets_received" "packets_sent" "receive_time" "serial_number" "session_id" "src_ip" "src_port"


| inputlookup firewall_traffic.csv | head 50000
| fit SVM  "used_by_malware" from "bytes_received" "bytes_sent" "dest_port" "dst_ip" "has_known_vulnerability" "packets_received" "packets_sent" "receive_time" "serial_number" "session_id" "src_ip" "src_port" into "_exp_draft_0e467230935543b98e7882eebdfce34d"

| inputlookup firewall_traffic.csv | head 50000
| fit RandomForestClassifier  "used_by_malware" from "bytes_received" "bytes_sent" "dest_port" "dst_ip" "has_known_vulnerability" "packets_received" "packets_sent" "receive_time" "serial_number" "session_id" "src_ip" "src_port" into "_exp_draft_0e467230935543b98e7882eebdfce34d"

| inputlookup firewall_traffic.csv | head 50000
| fit GaussianNB  "used_by_malware" from "bytes_received" "bytes_sent" "dest_port" "dst_ip" "has_known_vulnerability" "packets_received" "packets_sent" "receive_time" "serial_number" "session_id" "src_ip" "src_port" into "_exp_draft_0e467230935543b98e7882eebdfce34d"
```

## Tutorial 1

The figure below outlines the access to Splunk for machine learning. For this select the link below and enter your username and password:

```
http://asecuritysite.com:8443
```

![Alt text](https://asecuritysite.com/public/asecuritysite_splunk.png)


### Anomaly Detection
In this section we will analyse some of the models used to detect anomalies. The figure below outlines the mapping of the Iris dataset. The dataset contains four types of flower, and which have different dimensions for the petal length, petal width, septal length and septal width.

![Alt text](https://asecuritysite.com/public/Iris_dataset_scatterplot.png)



1. Select the Search tab, and in the search facility, enter the following [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20LocalOutlierFactor%20petal_length%20petal_width%20n_neighbors%3D10%20algorithm%3Dkd_tree%20metric%3Dminkowski%20p%3D1%20contamination%3D0.14%20leaf_size%3D10&sid=1593689150.93&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics"):

```
| inputlookup iris.csv
| fit LocalOutlierFactor petal_length petal_width n_neighbors=10 algorithm=kd_tree metric=minkowski p=1 contamination=0.14 leaf_size=10
```


How many records are there?


What are the fields within the dataset:



What is the value assigned for outliers:


What is the value assigned for inliers:




2. Next we will run a One Class SVM model for anomaly detection [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20OneClassSVM%20*%20kernel%3D%22poly%22%20nu%3D0.5%20coef0%3D0.5%20gamma%3D0.5%20tol%3D1%20degree%3D3%20shrinking%3Df%20into%20TESTMODEL_OneClassSVM&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689268.98)

```
| inputlookup iris.csv
| fit OneClassSVM * kernel="poly" nu=0.5 coef0=0.5 gamma=0.5 tol=1 degree=3 shrinking=f into TESTMODEL_OneClassSVM
```


How many records are there?


Using petal_length and petal_width for the identification of an anomaly, determine the details of one flower with an anomaly:


Using petal_length and petal_width for the identification of an anomaly, determine the details of one flower with an anomaly:



3. We now will use a new data setup (call_center.csv) and run the Density Function method [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20call_center.csv%0A%7C%20fit%20DensityFunction%20count%20by%20%22source%22%20into%20mymodel&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689305.99)

```
| inputlookup call_center.csv
| fit DensityFunction count by "source" into mymodel
```


How many records are there?


What is the format of the stored data fields:


Outline one possible anomaly:




### Prediction (Categories)

4. We will go back to our Iris dataset, and run AutoPrediction [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20AutoPrediction%20random_state%3D42%20petal_length%20from%20*%20max_features%3D0.1%20into%20auto_classify_model%20test_split_ratio%3D0.3%20random_state%3D42&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689367.100)

```
| inputlookup iris.csv
| fit AutoPrediction random_state=42 petal_length from * max_features=0.1 into auto_classify_model test_split_ratio=0.3 random_state=42
```


Can you now train for sepal_length using sepal_width and petal_length. Outline one prediction for sepal_length (and the error from the actual value):



5. Now apply the BernoulliNB prediction model [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20BernoulliNB%20petal_length%20from%20*%20into%20TESTMODEL_BernoulliNB%20alpha%3D0.5%20binarize%3D0%20fit_prior%3Df&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689413.101)

```
| inputlookup iris.csv
| fit BernoulliNB petal_length from * into TESTMODEL_BernoulliNB alpha=0.5 binarize=0 fit_prior=f
```



Can you now train for petal_length using sepal_width and species. Outline one prediction for petal_length (and the error from the actual value):



6. Now apply the DecisionTreeClassifier prediction model [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20DecisionTreeClassifier%20petal_length%20from%20*%20into%20sla_%20MOD&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689514.102)

```
| inputlookup iris.csv
| fit DecisionTreeClassifier petal_length from * into sla_ MOD
```


Can you now train for petal_length using petal_width and species. Outline one prediction for petal_length (and the error from the actual value):
<br /><br />


7. Now apply the GaussianNB [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20GaussianNB%20petal_length%20from%20*%20into%20MOD&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689555.103)

```
| inputlookup iris.csv
| fit GaussianNB petal_length from * into MOD
```


Can you now train for petal_length using petal_width and species. Outline one prediction for petal_length (and the error from the actual value):



8. Now apply the GradientBoostingClassifier [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20GradientBoostingClassifier%20petal_length%20from%20*%20into%20MOD&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689603.104)

```
| inputlookup iris.csv
| fit GradientBoostingClassifier petal_length from * into MOD
```


Can you now train for petal_length using petal_width and species. Outline one prediction for petal_length (and the error from the actual value):



### Prediction (Numeric)

9. In the following we will use the track_day.csv data source. Perform an AutoPrediction model on batteryVoltage using longitudeGForce, speed and verticalGForce [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20AutoPrediction%20batteryVoltage%20target_type%3Dnumeric%20test_split_ratio%3D0.7%20from%20*%20into%20PM&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689674.105)

```
| inputlookup track_day.csv
| fit AutoPrediction batteryVoltage target_type=numeric test_split_ratio=0.7 from * into PM
```


Outline some of the features within the track_day data set:

Outline one prediction for batteryVoltage (and the error from the actual value):



10. Perform an DecisionTreeRegressor model on batteryVoltage using longitudeGForce, speed and verticalGForce [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20DecisionTreeRegressor%20batteryVoltage%20from%20*%20into%20PM&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689726.106)

```
| inputlookup track_day.csv
| fit DecisionTreeRegressor batteryVoltage from * into PM
```


Outline one prediction for batteryVoltage (and the error from the actual value):



11. Perform an ElasticNet model on batteryVoltage using longitudeGForce, speed and verticalGForce [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day_missing.csv%0A%7C%20fit%20ElasticNet%20batteryVoltage%20from%20*%20into%20EN&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689766.107)

```
| inputlookup track_day_missing.csv
| fit ElasticNet batteryVoltage from * into EN
```


Outline one prediction for batteryVoltage (and the error from the actual value):



12. Perform an GradientBoostingRegressor model on batteryVoltage using longitudeGForce, speed and verticalGForce [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day_missing.csv%0A%7C%20fit%20GradientBoostingRegressor%20batteryVoltage%20from%20*%20into%20GB&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689818.108)

```
| inputlookup track_day_missing.csv
| fit GradientBoostingRegressor batteryVoltage from * into GB
```


Outline one prediction for batteryVoltage (and the error from the actual value):



### Clustering

13. In the following we will use the iris.csv data source. Perform Birch clustering model on petal_length for three clusters [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20Birch%20petal_length%20k%3D3%20partial_fit%3Dtrue%20into%20MOD2&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593689910.110)

```
| inputlookup iris.csv
| fit Birch petal_length k=3 partial_fit=true into MOD2
```



Outline one value from each cluster:



14. In the following we will use the iris.csv data source. Perform DBSCAN clustering model on petal_length for three clusters [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20DBSCAN%20petal_length%20min_samples%3D4&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690004.112)

```
| inputlookup iris.csv
| fit DBSCAN petal_length min_samples=4
```



How many clusters have been created:

Now train on species, how many clusters are created, and how is the clustering setup:



15. In the following we will use the iris.csv data source. Perform GMeans clustering model on petal_length for three clusters [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20GMeans%20petal_length%20random_state%3D42%20into%20MOD3&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690050.113)

```
| inputlookup iris.csv
| fit GMeans petal_length random_state=42 into MOD3
```


How many clusters have been created:



16. In the following we will use the iris.csv data source. Perform GMeans clustering model on petal_length for three clusters [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20iris.csv%0A%7C%20fit%20KMeans%20%20petal_length%20k%3D3%20into%20MOD4&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690100.114)

```| inputlookup iris.csv
| fit KMeans  petal_length k=3 into MOD4
```


How many clusters have been created:



### Feature Extraction
17. In the following we will use the FieldSelector method to determine the best feature selector for batteryVoltage given engineCoolantTemperature, engineSpeed, lateralGForce,longitudeGForce, speed [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20FieldSelector%20batteryVoltage%20from%20engineCoolantTemperature%2C%20engineSpeed%2C%20lateralGForce%2ClongitudeGForce%2C%20speed%20type%3Dnumeric&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690196.116)

```
| inputlookup track_day.csv
| fit FieldSelector batteryVoltage from engineCoolantTemperature, engineSpeed, lateralGForce,longitudeGForce, speed type=numeric
```


Best feature:




18. Now we find the best feature for batteryVoltage for engineSpeed, lateralGForce and longitudeGForce [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20FieldSelector%20batteryVoltage%20from%20engineSpeed%2C%20lateralGForce%2ClongitudeGForce%2C%20speed%20type%3Dnumeric&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690304.117)

```
| inputlookup track_day.csv
| fit FieldSelector batteryVoltage from engineSpeed, lateralGForce,longitudeGForce, speed type=numeric
```


Best feature:




19. Now for vechicleType (and which is a category), determine its best match for engineCoolantTemperature, engineSpeed, lateralGForce,longitudeGForce, and speed [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20FieldSelector%20vehicleType%20from%20engineCoolantTemperature%2C%20engineSpeed%2C%20lateralGForce%2ClongitudeGForce%2C%20speed%20type%3Dcategorical&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690348.118)

```
| inputlookup track_day.csv
| fit FieldSelector vehicleType from engineCoolantTemperature, engineSpeed, lateralGForce,longitudeGForce, speed type=categorical
```


Best feature:




20. Within the best feature, we can use the HashingVectorization to analyse the difference between strings (using N-grams). Run the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20passwords.csv%0A%7C%20fit%20HashingVectorizer%20Passwords%20ngram_range%3D1-2%20k%3D10&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690411.119)

```
| inputlookup passwords.csv
| fit HashingVectorizer Passwords ngram_range=1-2 k=10
```


What is the data used in the dataset

For the tokens tried, which ones have been successful in finding password matches:



21. The ICA (Independent component analysis) method is used to reduce the number of dimensions in the data. Run the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20ICA%20batteryVoltage%2C%20engineSpeed%2C%20engineCoolantTemperature%09%20n_components%3D2%20as%20IC&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690452.120)

```
| inputlookup track_day.csv
| fit ICA batteryVoltage, engineSpeed, engineCoolantTemperature	 n_components=2 as IC
```


What do you observe from the output:

What happens when you change n_components to 1:



22.  We can do the same reduction with PCA. Run the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20KernelPCA%20batteryVoltage%2C%20engineSpeed%2C%20engineCoolantTemperature%20k%3D2%20gamma%3D0.001%20as%20PCA&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690503.121)


```
| inputlookup track_day.csv
| fit KernelPCA batteryVoltage, engineSpeed, engineCoolantTemperature k=2 gamma=0.001 as PCA
```


What do you observe from the output:

What happens when you change the k to 1:


23. NPR (Normalized Perlich Ratio) is useful in converting categorical fields into numeric values [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20NPR%20vehicleType%20%20from%20engineSpeed%20%20as%20npr01&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690576.122)

```
| inputlookup track_day.csv
| fit NPR vehicleType  from engineSpeed  as npr01
```


What do you observe from the output:



24. Principal Component Analysis (PCA) reduce the number of fields in the data. Run the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20PCA%20engineCoolantTemperature%2C%20engineSpeed%2C%20lateralGForce%2Cspeed%20k%3D2%20as%20pca01&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690710.123)

```
| inputlookup track_day.csv
| fit PCA engineCoolantTemperature, engineSpeed, lateralGForce,speed k=2 as pca01
```


What do you observe from the output:



25. TF-IDF (Term Frequency-Inverse Document Frequency) converts raw text data into a matrix, and can be used to find words within documents. Run the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day.csv%0A%7C%20fit%20TFIDF%20vehicleType%20ngram_range%3D1-2%20max_df%3D0.6%20min_df%3D0.2%20stop_words%3Denglish%20as%20tf01&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690755.124)

```| inputlookup track_day.csv
| fit TFIDF vehicleType ngram_range=1-2 max_df=0.6 min_df=0.2 stop_words=english as tf01
```


What do you observe from the output:



### Feature Extraction
25. We can Imputer to replace data that is missing. Enter the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day_missing.csv%0A%7C%20fit%20Imputer%20batteryVoltage&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690795.125)

```
| inputlookup track_day_missing.csv
| fit Imputer batteryVoltage
```


What data has been replaced:

We can also add a strategy or mean, median and most_frequent, what are the results when you add each of these:



26. RobustScaler scales to median and interquartile range to 0 and 1. It thus reduces the bias caused by large data ranges swamping smaller values.

```
| inputlookup track_day_missing.csv
| fit RobustScaler *
```


Outline the result:



27. Now try the ScandardScalar [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20track_day_missing.csv%0A%7C%20fit%20RobustScaler%20*&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690835.126)

```
| inputlookup track_day_missing.csv
| fit StandardScaler *
```



### Forecasting
28. A common method we have is to forecast over time. The StateSpaceForecast method is based on Kalman filters. Run the following query [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20app_usage.csv%0A%7C%20fit%20StateSpaceForecast%20CRM%20ERP%20Expenses%20holdback%3D12%20into%20SF&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690880.127)

```| inputlookup app_usage.csv
| fit StateSpaceForecast CRM ERP Expenses holdback=12 into SF
```


Outline the result:



29. Finally, we can use the ARIMA model for forecasting. Perform the following search [link](https://asecuritysite.com:8443/en-GB/app/Splunk_ML_Toolkit/search?q=%7C%20inputlookup%20logins.csv%0A%7C%20fit%20ARIMA%20_time%20logins%20holdback%3D0%20conf_interval%3D95%20order%3D0-0-0%20forecast_k%3D5%20as%20AR&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&display.page.search.tab=statistics&display.general.type=statistics&sid=1593690918.128)

```
| inputlookup logins.csv
| fit ARIMA _time logins holdback=0 conf_interval=95 order=0-0-0 forecast_k=5 as AR
```


Outline the result:
<br /><br />


## References
[1] https://en.wikipedia.org/wiki/Iris_flower_data_set




