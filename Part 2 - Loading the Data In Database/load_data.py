# Connecting Python to MySQL
import pymysql
import pandas as pd
countries_df = pd.read_csv('countries_df.csv')
customer_cc_df = pd.read_csv('customer_cc_df.csv')
product_df = pd.read_csv('product_df .csv')
department_df = pd.read_csv('department_df.csv')
customer_df = pd.read_csv('customer_df.csv')
employee_df = pd.read_csv('employee_df.csv')
payment_df = pd.read_csv('payment_df.csv')

'''
1. Connecting Python to postgres
'''

connection = pymysql.connect(host ='localhost',port=int(5432),user='postgres',passwd='Ayoub1234@')
print("connection good")

# Creating a cursor object
cursor = connection.cursor()

'''
2. Creating a new Schema 
'''

# Create a new schema called whiskey_shop
cursor.execute('''
drop schema if exists ecom;
''')

cursor.execute('''
create schema ecom;
''')

# Use the new schema
cursor.execute('''
use ecom;
''')

'''
3. Generating empty tables
'''
# Countries
cursor.execute('''
DROP TABLE IF EXISTS countries;
''')

cursor.execute('''
CREATE TABLE countries (
    country VARCHAR(100) NOT NULL,
    country_code VARCHAR(100) NOT NULL,
    country_id INT PRIMARY KEY
    );
''')

# Customer_cc
cursor.execute('''
DROP TABLE IF EXISTS customer_cc;
''')

cursor.execute('''
CREATE TABLE customer_cc (
    credit_provider VARCHAR(100) NOT NULL,
    credit_provider_id INT PRIMARY KEY
    );
''')

# Products
cursor.execute('''
DROP TABLE IF EXISTS products;
''')

cursor.execute('''
CREATE TABLE products (
    Product_Name VARCHAR(100) NOT NULL,
    Caffeine_Content_mg FLOAT NOT NULL,
    Price_USD FLOAT NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Sugar_Content_g FLOAT NOT NULL,
    product_id INT NOT NULL PRIMARY KEY
);

''')

# Departments
cursor.execute('''
DROP TABLE IF EXISTS departments;
''')

cursor.execute('''
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department VARCHAR(100) NOT NULL
    );
''')

# Customers
cursor.execute('''
DROP TABLE IF EXISTS customers;
''')

cursor.execute('''
CREATE TABLE customers (
    customer_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    street VARCHAR(100) NOT NULL,
    four_digits INT NOT NULL,
    country_id INT NOT NULL,
    credit_provider_id INT NOT NULL,
    
    FOREIGN KEY (country_id) REFERENCES countries (country_id),
    FOREIGN KEY (credit_provider_id) REFERENCES customer_cc (credit_provider_id)
);

''')

# Employees
cursor.execute('''
DROP TABLE IF EXISTS employees;
''')

cursor.execute('''
CREATE TABLE employees (
    employee_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

''')

# Payments
cursor.execute('''
DROP TABLE IF EXISTS payments;
''')

cursor.execute('''
CREATE TABLE payments (
    payment_id INT NOT NULL PRIMARY KEY,
    date DATETIME NOT NULL,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    product_id INT NOT NULL,
    price FLOAT NOT NULL,
    
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

''')
print("creating table go")
# Make sure the DataFrame columns are correct and match the expected SQL columns.
print(customer_cc_df.head())
print(product_df.head())
print(department_df.head())
print(customer_df.head())
print(employee_df.head())
print(payment_df.head())

# Inserting Data
'''
4. Inserting Data
'''

# Countries
for data in countries_df.itertuples(index=False):
    query = "INSERT INTO countries (country, country_code, country_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (data.country, data.country_code, data.country_id))

# Customer_cc
for data in customer_cc_df.itertuples(index=False):
    query = "INSERT INTO customer_cc (credit_provider, credit_provider_id) VALUES (%s, %s)"
    cursor.execute(query, (data.credit_provider, data.credit_provider_id))

# Products
# Products
for data in product_df.itertuples(index=False):
    query = "INSERT INTO products (Product_Name, Caffeine_Content_mg, Price_USD, Country, Sugar_Content_g, product_id) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data.Product_Name, data.Caffeine_Content_mg, data.Price_USD, data.Country, data.Sugar_Content_g, data.product_id))

# Departments
for data in department_df.itertuples(index=False):
    query = "INSERT INTO departments (department_id, department) VALUES (%s, %s)"
    cursor.execute(query, (data.department_id, data.department))

# Customers
for data in customer_df.itertuples(index=False):
    query = "INSERT INTO customers (customer_id, first_name, last_name, full_name, email, street, four_digits, country_id, credit_provider_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data.customer_id, data.first_name, data.last_name, data.full_name, data.email, data.street, data.four_digits, data.country_id, data.credit_provider_id))

# Employees
for data in employee_df.itertuples(index=False):
    query = "INSERT INTO employees (employee_id, first_name, last_name, full_name, email, city, department_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data.employee_id, data.first_name, data.last_name, data.full_name, data.email, data.city, data.department_id))

# Payments
# Payments
for data in payment_df.itertuples(index=False):
    query = "INSERT INTO payments (payment_id, date, customer_id, employee_id, product_id, price) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data.payment_id, data.date, data.customer_id, data.employee_id, data.product_id, data.price))

# Commit the transaction after all inserts
connection.commit()
# Close the cursor and the connection
cursor.close()
connection.close()
print("Data inserted successfully and connection closed.")