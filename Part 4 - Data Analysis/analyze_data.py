import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import pandasql as ps
from empiricaldist import Pmf
plt.style.use('ggplot')
sns.set_palette('Blues_r')
sns.set_context('notebook')

def mysql(query):
    return pd.read_sql_query(query, connection)

def sql(query):
    return ps.sqldf(query)
  
'''
Connecting to MySQL
'''
# Creating a connection object
connection = pymysql.connect(host ='localhost',
                             port=int(3306),
                             user='root',
                             passwd='',
                             db='dwh_ecom')

# Creating a cursor object
cursor = connection.cursor()
print("Connection established!")

'''
Pulling Data for Analysis
'''
# Creating the query
# Creating the query for the dwh_ecom fact table and related tables
query = '''
SELECT 
    f.date,
    d.Day_name AS Day,
    d.Month_name AS Month,
    d.Year_name AS Year,
    p.Product_Name,
    f.Price_USD, 
    p.Caffeine_Content_mg,
    f.Sugar_Content_g,
    c.full_name AS customer_name,
    co.Country AS customer_country,
    f.credit_provider,  -- Adjust if you have this field in your fact table
    e.full_name AS employee_name
FROM 
    dwh_ecom.dwh_fact AS f
LEFT JOIN 
    ecom.customers AS c ON f.customer_id = c.customer_id
LEFT JOIN 
    ecom.countries AS co ON c.country_id = co.country_id  -- Replace with correct country table
LEFT JOIN 
    ecom.employees AS e ON e.employee_id = f.employee_id
LEFT JOIN 
    dwh_date AS d ON d.Date_key = f.Date_key
LEFT JOIN 
    dwh_products AS p ON f.product_id = p.product_id  -- Added this line to join the products table
ORDER BY 
    f.date;
'''

# Generating a DataFrame according to the query
df = mysql(query)

# Displaying the first few rows of the DataFrame
print(df.head())


'''
Pre-Processing
'''
# Extracting a list of column
df_columns = df.columns.to_list()

# Iterating through the columns
for column in df_columns:
    
    # If the column is date, change the data type to datetime
    if column == 'date':
        df[column] = pd.to_datetime(df[column])
    
    # If the column is object, change the data type to category
    if df[column].dtype == 'object':
        df[column] = df[column].astype('category')
        
print(df.dtypes)       
'''
Q1 — Which products produce the most profit?
'''
# Generating a Dataframe containing the 5 most profitable products
query = '''
select 
    count(*) as Number_Of_Transactions, 
    Product_Name, 
    sum(Price_USD) as Profit
    
from df
group by Product_Name
order by sum(Price_USD) desc
limit 5
'''

top_5_products = sql(query)
colors = ['green'] + ['orange'] * (len(top_5_products) - 1) 

sns.catplot(data = top_5_products, x = 'Product_Name', y = 'Profit', 
            kind = 'bar', palette=colors, height = 5, aspect = 2)
plt.xlabel('Product Name',size = 16)
plt.xlabel('Profit',size = 16)

plt.title('Top 5 Most Profitable Products',size = 18)
plt.savefig('top_5_most_profitable_products.png', dpi=300, bbox_inches='tight')
#plt.show()



'''
Q2 — Which products people usually buy?
'''
# Extracting the most commonly sold products
query = '''
SELECT 
    COUNT(*) AS Number_Of_Transactions, 
    Product_Name
FROM df
GROUP BY Product_Name
ORDER BY COUNT(*) DESC
'''

most_bought_products = sql(query)

# Generating a PMF
prob_mass_func = pd.DataFrame(Pmf.from_seq(df.Product_Name))

# Sorting 
sorted_prob_mass_func = prob_mass_func.iloc[:,0].sort_values(ascending = False)

# Filtering only the top 1 percentile of products
sorted_prob_mass_func = sorted_prob_mass_func[sorted_prob_mass_func > sorted_prob_mass_func.quantile(0.99)]

# Generating a Dataframe
probablity_Dataframe = pd.DataFrame()
probablity_Dataframe['Product'] = sorted_prob_mass_func.index
probablity_Dataframe['Probablity to Buy'] = sorted_prob_mass_func.values

# Output
print(probablity_Dataframe)
'''
result:
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
'''


'''
Q3 — Are there any interesting patterns as to when customers like to buy energy drinks? If so, what are they?
'''
query = '''
SELECT 
    COUNT(*) AS Number_Of_Transactions, 
    Day
FROM df
GROUP BY Day
ORDER BY Number_Of_Transactions
'''

most_bought_products_by_day = sql(query)

# Plotting
sns.catplot(data=most_bought_products_by_day, 
            y='Number_Of_Transactions', x='Day',  # Ensure 'Day' matches the SQL output
            kind='bar', height=6, aspect=3)

plt.xlabel('Day', size=18)
plt.ylabel('Number Of Transactions', size=18)
plt.title('Number of Transactions vs Day', size=22)

# Save the plot as an image
plt.savefig('energy_drink_sales_by_day.png', bbox_inches='tight')

#plt.show()


#FOR MONTH

query = '''
select 
    count(*) as Number_Of_Transactions, 
    Day,
    month
    
from df
group by month,Day
order by count(*) desc
'''

most_bought_products_by_month = sql(query)
# Define a color palette for different months
color_palette = sns.color_palette("husl", n_colors=most_bought_products_by_month['Month'].nunique())

# Generate the catplot with a color for each month
g = sns.catplot(data=most_bought_products_by_month, 
                y='Number_Of_Transactions', 
                x='Month', 
                kind='bar', 
                height=6, 
                aspect=3,
                palette=color_palette)

# Adding labels and title
plt.xlabel('Month', size=18)
plt.ylabel('Number_Of_Transactions', size=18)
plt.title('Number of Transactions vs Month', size=22)

# Save the plot as a PNG file
plt.savefig('transactions_vs_month.png', format='png')

# Show the plot
#plt.show()


'''
Q4 — Are we growing as a company in terms of profits or not?
'''

query = '''
select 
    sum(Price_USD) as Profit, 
    year
    
from df
where year != 2022
group by year
order by year asc
'''

profits_by_year = sql(query)

x = profits_by_year.Year
y = np.cumsum(profits_by_year.Profit)

plt.rcParams["figure.figsize"] = [15, 8]
plt.rcParams["figure.autolayout"] = True
plt.plot(x,y)
plt.xlabel('Year', size = 16)
plt.ylabel('Profit(in Millions)', size = 16)
plt.title('Cummulative Profit', size = 20)
#plt.show()


print(df.columns)

'''
Q5 — From which countries do most of the customers come from
'''
# Query to get the number of customers by country
query = '''
SELECT 
    COUNT(DISTINCT customer_name) AS Number_of_customers, 
    customer_country
FROM df
GROUP BY customer_country
ORDER BY customer_country ASC
'''


customers_by_country = sql(query)

# Filtering the top ten countries by customer count
top_ten_percentile = customers_by_country.sort_values(by='Number_of_customers', ascending=False).head(10)


# Print the results
print(top_ten_percentile)
palette = sns.color_palette("husl", len(top_ten_percentile))
# Generating the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_ten_percentile, x='Number_of_customers', y='customer_country', palette=palette)
plt.title('Top 10 Countries by Number of Customers')
plt.xlabel('Number of Customers')
plt.ylabel('Country')
#plt.show()

# Save the plot as a PNG file
plt.savefig('top_countries_by_customers.png', format='png')

# Show the plot
#plt.show()
