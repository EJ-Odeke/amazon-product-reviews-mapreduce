# amazon-product-reviews-mapreduce
## Project Title:
### **MapReduce Analysis of Amazon Fine Food Reviews using mrjob**

**Project Summary**

This project applies the MapReduce programming model using the mrjob Python library to perform scalable analysis on a large Amazon product review dataset. Specifically, it analyzes the Musical Instruments category from the Amazon Review Data (2018), which contains 1,512,530 reviews across 120,400 products.
The project demonstrates end-to-end big data processing — from data preparation to distributed computation — to extract meaningful business insights such as product popularity, customer satisfaction levels, and review quality. All MapReduce jobs were implemented in Python with mrjob, enabling seamless execution locally, on Hadoop, or on cloud platforms like Amazon Elastic MapReduce (EMR).

**Dataset**

Source: Amazon Review Data (2018) by Julian McAuley, UCSD
Category: Musical Instruments
Size: 1,512,530 reviews | 120,400 products
Time Period: Reviews up to October 2018
Key Fields: reviewerID, asin (Product ID), overall (star rating), reviewText, helpful (votes), unixReviewTime, etc.
Dataset Link: https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/ (Musical Instruments category)

**Objectives**

Implement multiple MapReduce jobs to compute key metrics from a large-scale review dataset.
Demonstrate data aggregation, numerical computation, and ranking using the MapReduce paradigm.
Derive actionable insights for e-commerce product performance and customer feedback analysis.

**Technologies & Tools**

Programming Language: Python
MapReduce Framework: mrjob library
Development & Testing: Local mode + Hadoop/EMR
Data Handling: Python (Pandas for exploration), JSON parsing


