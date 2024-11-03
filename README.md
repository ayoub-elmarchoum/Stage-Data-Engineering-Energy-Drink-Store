# Data-Engineering-Project-energy drinks  -Store
In this project, I created an __entire data architecture__ for a made-up energy drinks Retail  shop that will enable shop managers to make decisions based on their data. 
This project will simulate the entire process that data-driven companies do to make data-based decisions.

__The project will include Web Scraping, processing and transforming data, loading and designing a Database and a Data Warehouse, and finally, analysis and descision making.__

## Project Architecture
![document](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/Project%20Architecture.jpg)


## Part 1 - Web Scraping
In this part I web scraped whisky product data from EnergyDrinks.

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

2. Exported CSV files of each type of Energy Drink




**********************************************************************************************************************************
**********************************************************************************************************************************
**********************************************************************************************************************************

## Part 2 - Loading the Data
In this part, I generated data about the energy drinks restail shop, designed a Central RDBMS, applied normalization to the data and loaded it.

## Applying the code
1. Generate Random Data

```
python generate_store_data.py
```

2. Design the Database

- Current Schema:

![current_schema](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/images%20for%20github/Current%20Schema.svg)


- Run this to design the data
```
python normalize_data.py
```

- Finished Schema:

![Finished Schema](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/images%20for%20github/Finished%20Schema.jpg)

3. Load the Data to MySQL
```
Python load_data.py
```

## End Result
All the Data is now stored in MySQL.

![endSchema](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/images%20for%20github/endSchema.jpg)



**********************************************************************************************************************************
**********************************************************************************************************************************
**********************************************************************************************************************************

## Part 3 - Designing a Data Warehouse
In this part, I will design a Data Warehouse which will be the main analytic focal point of the company. 

I'll create a fact table and various dimensions for the Data Warehouse such as Date, Customers, Employees and Products Dimension.

I will also create multiple triggers that will handle the transfer of data between the company's central Database and the Data Warehouse.

## Applying the code

### In Python - Generate the Date Dimension

```
python generate_date_dim.py
```

### In MySQL - Generate Dimensions & Triggers

```
generate_customers_dim.sql
generate_employee_dim.sql
generate_product_dim.sql
generate_fact_table.sql

triggers.sql
```
### Finished Data Warehouse Schema:
[![dwh_ecom](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink Store/blob/main/images%20for%20github/datawarehouse_ecom.jpg)
![dwh_ecom1](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/images%20for%20github/dwh_ecom.jpg)

**********************************************************************************************************************************
**********************************************************************************************************************************
**********************************************************************************************************************************

# Part 4 - Analyzing the Data
In this part, ill get into the shoes of the analysts in the company and analyze the data in the Data Warehouse.

### Applying the code
```
python analyze_data.py
```

### End Result  Data Analysis

1. Q1 — Which types of energy drinks produce the most profit?

![Q1](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/Part%204%20-%20Data%20Analysis/top_5_most_profitable_products.png)
2. Q2 — Which types of whisky people usually buy?
result:
```
Product                         Probablity to Buy
0   Energy Drink X 46             0.002385
1   Energy Drink L 14             0.002031
2   Energy Drink D 75             0.001855
3    Energy Drink T 3             0.001766
0   Energy Drink X 46             0.002385
1   Energy Drink L 14             0.002031
2   Energy Drink D 75             0.001855
3    Energy Drink T 3             0.001766
1   Energy Drink L 14             0.002031
2   Energy Drink D 75             0.001855
3    Energy Drink T 3             0.001766
2   Energy Drink D 75             0.001855
3    Energy Drink T 3             0.001766
3    Energy Drink T 3             0.001766
4   Energy Drink H 66             0.001678
4   Energy Drink H 66             0.001678
5   Energy Drink F 41             0.001678
6   Energy Drink U 22             0.001590
7   Energy Drink E 50             0.001590
8   Energy Drink L 20             0.001590
9   Energy Drink D 74             0.001590
10   Energy Drink X 9             0.001590

interpration : 
The table shows the top 1 percentile of most commonly sold products. 
For instance, Energy Drink X has a 0.2385% chance of being purchased by a random customer,
indicating strong popularity. Similarly, Energy Drink L and D follow with 
probabilities of 0.2031% and 0.1855%, respectively. Lastly, Energy Drink T hasa 0.1766% chance,
 suggesting it remains a viable option but is less favored compared to the others.
```



3. Question 3 — Are there any interesting patterns as to when customers like to buy whiskey? If so what are they?

![Q3](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/Part%204%20-%20Data%20Analysis/transactions_vs_month.png)
![Q3](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/Part%204%20-%20Data%20Analysis/energy_drink_sales_by_day.png)
4. Q4 — Are we growing as a company in terms of profits or not?
![Q4](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/Part%204%20-%20Data%20Analysis/Cumulative_Profit.png)


5. Q5 — From which counties do most of the customers come from
![Q5](https://github.com/ayoub-elmarchoum/Stage-Data-Engineering-Energy-Drink-Store/blob/main/Part%204%20-%20Data%20Analysis/top_countries_by_customers.png)

