import numpy as np
import pandas as pd
import names
from faker import Faker
faker = Faker()
import pandasql as ps
import random
import time
from datetime import datetime
import pandas as pd
import numpy as np
import random

def sql(query):
    return ps.sqldf(query)



# Define sample values for each column
product_names = ["Energy Drink " + chr(i) for i in range(65, 91)]  # Energy Drink A to Z
countries = ["USA", "Germany", "France", "Japan", "South Korea", "UK", "Canada"]
caffeine_content = np.round(np.random.uniform(50, 300, 4000), 1)  # Caffeine in mg
prices = np.round(np.random.uniform(1, 10, 4000), 2)  # Prices between $1 and $10
sugar_content = np.round(np.random.uniform(0, 50, 4000), 1)  # Sugar content in grams

# Create the DataFrame
data = {
    "Product_Name": [random.choice(product_names) + " " + str(random.randint(1, 100)) for _ in range(4000)],
    "Caffeine_Content_mg": caffeine_content,
    "Price_USD": prices,
    "Country": [random.choice(countries) for _ in range(4000)],
    "Sugar_Content_g": sugar_content,
}

# Generate and save the DataFrame
product_df  = pd.DataFrame(data)
# Generate a column of unique product ids
product_id = np.random.default_rng().choice(len(product_df.Product_Name), len(product_df.Product_Name), replace=False)

# Verify that there are as many ids as there are products
assert len(set(product_id)) == len(product_df.Product_Name), "IDs are not unique!"

# Verify that the new ids are unique
assert len(pd.Series(product_id).unique()) == len(product_id), "Duplicate IDs found!"

# Insert the new column into the dataframe
product_df['product_id'] = product_id

# Display the updated DataFrame
print(product_df)

product_df .to_csv('product_df .csv', index=False)

print("Generated 'product_df .csv' with 4,000 rows.")
energy_drink_df = pd.read_csv('product_df .csv')
print(product_df .head())

'''
Generating Employee Data
'''

# Initialize Faker
faker = Faker()

# Set the number of employees
num_employees = 100

# Generate 100 unique employee IDs
employee_id = np.random.default_rng().choice(4000, num_employees, replace=False)

# Verify that there are as many ids as there are employees
assert len(set(employee_id)) == num_employees

# Verify that the new ids are unique
assert len(pd.Series(employee_id).unique()) == len(employee_id)

# Lists to store employee data
employee_first_name = []
employee_last_name = []
employee_full_name = []
employee_email = []
employee_city = []
departments = ['Sales', 'Finance', 'Marketing', 'BI']
employee_department = []

# Iterate through the employees and generate random data
for i in range(num_employees):
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    employee_first_name.append(first_name)
    employee_last_name.append(last_name)
    employee_full_name.append(f"{first_name} {last_name}")
    employee_email.append(f"{first_name}{last_name[0].lower()}@gmail.com")
    employee_city.append(faker.city())
    employee_department.append(np.random.choice(departments, 1)[0])

# Create the employee DataFrame directly from a dictionary
employee_df = pd.DataFrame({
    'employee_id': employee_id,
    'first_name': employee_first_name,
    'last_name': employee_last_name,
    'full_name': employee_full_name,
    'email': employee_email,
    'city': employee_city,
    'department': employee_department,
})
    # Display the first few rows of the employee DataFrame
employee_df.to_csv('employee_df.csv', index=False)
print("Saved 'employee_df.csv' with 100 rows.")
print(employee_df.head())
'''
Generating Customer Data
'''

# Initialize Faker
faker = Faker()

# Set the number of customers
num_customers = 1000

# Generating 1000 Unique Customer IDs
customer_id = np.random.default_rng().choice(999999, num_customers, replace=False)

# Verify that there are as many IDs as there are customers
assert len(set(customer_id)) == num_customers
assert len(pd.Series(customer_id).unique()) == len(customer_id)

# Lists to store customer data
customer_first_name = []
customer_last_name = []
customer_full_name = []
customer_email = []
customer_last_four_digits = []
customer_country = []
customer_country_code = []
customer_street = []
customer_credit_card_company = []

# Iterate through the customers and generate random data
for _ in range(num_customers):
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    customer_first_name.append(first_name)
    customer_last_name.append(last_name)
    customer_full_name.append(f"{first_name} {last_name}")
    customer_email.append(f"{first_name}{last_name[0].lower()}@gmail.com")
    customer_last_four_digits.append(np.random.randint(1000, 10000))  # Random 4-digit number
    country = faker.country()
    customer_country.append(country)
    customer_country_code.append(country[0:3].upper())  # Extract the first three letters of the country
    customer_street.append(faker.street_address())
    customer_credit_card_company.append(faker.credit_card_provider())

# Create a customer DataFrame directly from a dictionary
customer_df = pd.DataFrame({
    'customer_id': customer_id,
    'first_name': customer_first_name,
    'last_name': customer_last_name,
    'full_name': customer_full_name,
    'email': customer_email,
    'country': customer_country,
    'country_code': customer_country_code,
    'street': customer_street,
    'credit_provider': customer_credit_card_company,
    'four_digits': customer_last_four_digits
})
# Display the first few rows of the customer DataFrame
customer_df.to_csv('customer_df.csv', index=False)
print("Saved 'customer_df.csv' with 1,000 rows.")
print(customer_df.head())
    
'''
Generating Payments Data
'''
# Étape 1 : Générer une plage de dates de 1990 à 2020
date_range = pd.date_range(start="1990-01-01", end="2020-12-31", freq="D")

# Supposons que vous ayez déjà les DataFrames product_df, customer_df et employee_df

# Étape 2 : Générer des identifiants de paiement uniques
payment_id = np.random.default_rng().choice(999999, len(date_range), replace=False)

# Vérifier qu'il y a autant d'ids qu'il y a de dates
assert len(set(payment_id)) == len(date_range)
assert len(pd.Series(payment_id).unique()) == len(payment_id)

# Étape 3 : Générer les données de paiement
customer_id_payments = []
employee_id_payments = []
product_id_payments = []
dates = []

# itérer à travers les paiements et générer des données aléatoires
for _ in range(len(payment_id)):
    dates.append(random.choice(date_range))  # Choisir une date aléatoire
    customer_id_payments.append(random.choice(customer_df['customer_id']))  # ID client aléatoire
    employee_id_payments.append(random.choice(employee_df['employee_id']))  # ID employé aléatoire
    product_id_payments.append(random.choice(product_df['product_id']))  # ID produit aléatoire

# Étape 4 : Créer un DataFrame de paiements
payment_df = pd.DataFrame({
    'payment_id': payment_id,
    'date': dates,
    'customer_id': customer_id_payments,
    'employee_id': employee_id_payments,
    'product_id': product_id_payments
})

# Étape 5 : Ajouter la colonne de prix des produits
# Supposons que product_df ait une colonne 'Price_USD' pour le prix
payment_df = payment_df.merge(product_df[['product_id', 'Price_USD']], on='product_id', how='inner')




# Adding the Alcohol_price column to the table
query = """
SELECT p1.*, p2.Price_USD as price
FROM payment_df p1
INNER JOIN product_df p2
ON p1.product_id = p2.product_id
"""

payment_df = sql(query)
payment_df.to_csv('payment_df.csv', index=False)
print("Saved 'payment_df.csv' with payment transactions.")