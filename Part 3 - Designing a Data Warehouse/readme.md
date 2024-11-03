# Part 3 - Designing a Data Warehouse
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
