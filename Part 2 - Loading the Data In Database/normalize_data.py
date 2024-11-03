import pandas as pd
from pandasql import sqldf

sql = lambda q: sqldf(q, globals())
customer_df = pd.read_csv('customer_df.csv')
employee_df = pd.read_csv('employee_df.csv')
product_df = pd.read_csv('product_df .csv')
payment_df = pd.read_csv('payment_df.csv')

# Creating a new table called countries
unique_countries = customer_df['country'].unique()
countries_df = pd.DataFrame(unique_countries, columns=['country'])
countries_df['country_code'] = countries_df['country'].str[0:3].str.upper()
countries_df['country_id'] = range(len(countries_df))

# Extracting the country_id column from customers
# Ensure customer_df has 'country_code' column for the join
query = '''
SELECT countries_df.country_id
FROM customer_df
JOIN countries_df
ON customer_df.country_code = countries_df.country_code
AND customer_df.country = countries_df.country
'''
country_ids = sql(query)

# Adding the foreign key: country_id to customer_df
customer_df['country_id'] = country_ids

# Dropping the columns 'country' and 'country_code' from customer_df
customer_df = customer_df.drop(['country', 'country_code'], axis=1)

# Creating a new table called customer_cc for unique credit providers
unique_cc_providers = customer_df['credit_provider'].unique()
customer_cc_df = pd.DataFrame(unique_cc_providers, columns=['credit_provider'])
customer_cc_df['credit_provider_id'] = range(len(customer_cc_df))

# Extracting the credit_provider_id column from customers
query = '''
SELECT customer_cc_df.credit_provider_id
FROM customer_df
JOIN customer_cc_df
ON customer_df.credit_provider = customer_cc_df.credit_provider
'''
credit_provider_ids = sql(query)

# Adding the foreign key: credit_provider_id to customer_df
customer_df['credit_provider_id'] = credit_provider_ids

# Dropping the column 'credit_provider' from customer_df
customer_df = customer_df.drop(['credit_provider'], axis=1)

# Display the final tables for verification
print("Countries DataFrame:\n", countries_df.head())
print("Customer Credit Providers DataFrame:\n", customer_cc_df.head())
print("Customer DataFrame:\n", customer_df.head())

'''
Normalizing the Employees Table
'''
# Extracting the departments from the employees table
departments = pd.Series(employee_df.department.unique()).to_list()

# Generating unique department ids
department_id = [*range(0, len(departments))]

# Creating a table called departments
department_df = pd.DataFrame(department_id, columns=['department_id'])
department_df['department'] = departments

# Extracting the country_id column from customers
query = '''
select department_df.department_id
from employee_df 
join department_df
on 
    employee_df.department = department_df.department
'''

department_ids = sql(query)

# Connecting countries to customers by adding the foregin key: country_id
employee_df['department_id'] = department_ids

# Dropping the column department
employee_df = employee_df.drop('department',axis = 1)

# Saving the countries DataFrame to a CSV file
countries_df.to_csv('countries_df.csv', index=False)

# Saving the customer credit providers DataFrame to a CSV file
customer_cc_df.to_csv('customer_cc_df.csv', index=False)

# Saving the updated customer DataFrame to a CSV file
customer_df.to_csv('customer_df.csv', index=False)

# Saving the updated employee DataFrame to a CSV file
employee_df.to_csv('employee_df.csv', index=False)
department_df.to_csv('department_df.csv', index=False) 

print("DataFrames saved to CSV files successfully.")


