# Part 1 - Web Scraping
In this part I web scraped product data.

I am excited to share that due to restrictions on scraping data from the website, 
I have generated random data for this project. Despite this limitation, the objectives
and steps remain unchanged. My goal is to apply data engineering concepts by 
creating an ETL pipeline and analyzing the data while implementing best practices 
in database management, including triggers and more.


Run this to apply the code:

```
python Scrape_data.py

```

## End Result

1. Panda's DataFrame with product data:
```
Product_Name        | Caffeine_Content_mg | Price_USD | Country | Sugar_Content_g
----------------------------------------------------------------------------------
Energy Drink G     |           68        |   92.2    | France  |     1.8
Energy Drink F     |           33        |  205.9    | France  |    39.7
Energy Drink V     |           72        |  137.1    | Germany |    24.0
Energy Drink R     |           33        |  106.8    | Canada  |     8.0
Energy Drink F     |           57        |  148.9    | Germany |    10.4
....
....

```

2. Exported CSV files of each type of Energy Drink :


