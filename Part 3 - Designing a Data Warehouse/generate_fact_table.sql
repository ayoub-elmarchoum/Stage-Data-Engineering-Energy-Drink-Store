-- Create a new fact table: dwh_fact
DROP TABLE IF EXISTS dwh_fact;

CREATE TABLE dwh_fact AS 
SELECT 
    c1.customer_id,
    e1.employee_id,
    p2.product_id,
    p2.Price_USD,  -- Assuming price is a column in the products table
    p2.Caffeine_Content_mg,  -- Using the correct column name for caffeine content
    p2.Sugar_Content_g,      -- Using the correct column name for sugar content
    c2.country_code AS Country,  -- Getting country code from the countries table
    d.Date_key,
    p1.date 
FROM
    ecom.payments AS p1
        JOIN
    ecom.customers AS c1 ON p1.customer_id = c1.customer_id
        JOIN
    ecom.employees AS e1 ON p1.employee_id = e1.employee_id
        JOIN
    ecom.products AS p2 ON p1.product_id = p2.product_id
        JOIN
    ecom.countries AS c2 ON c1.country_id = c2.country_id  -- Join on country_id
        JOIN
    dwh_date AS d ON p1.date = d.Dates
ORDER BY d.Dates;

-- Setting the foreign keys for each dimension table
ALTER TABLE dwh_fact
ADD FOREIGN KEY (customer_id) REFERENCES dwh_customers (customer_id);

ALTER TABLE dwh_fact
ADD FOREIGN KEY (employee_id) REFERENCES dwh_employees (employee_id);

ALTER TABLE dwh_fact
ADD FOREIGN KEY (product_id) REFERENCES dwh_products (product_id);

ALTER TABLE dwh_fact
ADD FOREIGN KEY (Date_key) REFERENCES dwh_date (Date_key);
