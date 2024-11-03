-- Dropping the dwh_products table if it exists
DROP TABLE IF EXISTS dwh_products;

-- Creating the dwh_products table and inserting data from ecom.products
CREATE TABLE dwh_products AS
SELECT 
    product_id,             
    Product_Name,            
    Caffeine_Content_mg,      
    Price_USD,                
    Sugar_Content_g,          
    Country                   
FROM 
    ecom.products 
ORDER BY 
    product_id;

-- Setting product_id as the primary key
ALTER TABLE dwh_products
MODIFY COLUMN product_id INT NOT NULL PRIMARY KEY;