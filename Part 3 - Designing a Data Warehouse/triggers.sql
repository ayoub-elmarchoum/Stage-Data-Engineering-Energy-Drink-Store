

--Create trigger insert_customer
DELIMITER //

CREATE TRIGGER insert_customer
AFTER INSERT ON customers  -- Utilise simplement le nom de la table, pas le schéma
FOR EACH ROW
BEGIN
    INSERT INTO dwh_ecom.dwh_customers (customer_id, first_name, last_name, full_name, country_code)
    SELECT 
        NEW.customer_id,
        NEW.first_name,
        NEW.last_name,
        NEW.full_name,
        c2.country_code
    FROM countries AS c2  -- Utilise simplement le nom de la table
    WHERE c2.country_id = NEW.country_id;
END; //

DELIMITER ;

--Create trigger insert_employee
DELIMITER //
CREATE TRIGGER insert_employee
AFTER INSERT ON ecom.employees
FOR EACH ROW
BEGIN
    INSERT INTO dwh_ecom.dwh_employees (employee_id, first_name, last_name, full_name, department)
    SELECT 
        NEW.employee_id,
        NEW.first_name,
        NEW.last_name,
        NEW.full_name,
        d.department
    FROM ecom.departments AS d
    WHERE d.department_id = NEW.department_id;
END; //
DELIMITER ;



-- Changer le délimiteur pour permettre l'utilisation de BEGIN...END
DELIMITER //

-- Supprimer le trigger s'il existe déjà
DROP TRIGGER IF EXISTS ecom.new_payment //

-- Créer le trigger new_payment après une insertion dans la table ecom.payments
CREATE TRIGGER ecom.new_payment
AFTER INSERT ON ecom.payments
FOR EACH ROW
BEGIN
    -- Insertion dans la table de faits de l'entrepôt de données
    INSERT INTO dwh_ecom.dwh_fact (
        customer_id,
        employee_id,
        product_id,
        Price_USD,
        Caffeine_Content_mg,
        Sugar_Content_g,
        Country,
        Date_key,
        date
    )
    SELECT 
        c.customer_id,           
        e.employee_id,           
        pr.product_id,          
        NEW.price,               
        pr.Caffeine_Content_mg,  
        pr.Sugar_Content_g,      
        co.Country,              
        d.Date_key,              
        NEW.date                 
    FROM ecom.customers AS c
    JOIN ecom.countries AS co ON c.country_id = co.country_id
    JOIN ecom.employees AS e ON NEW.employee_id = e.employee_id
    JOIN ecom.products AS pr ON NEW.product_id = pr.product_id
    JOIN dwh_ecom.dwh_date AS d ON DATE(d.Dates) = DATE(NEW.date)
    WHERE c.customer_id = NEW.customer_id;
END //


DELIMITER ;


--pour tester voila exemple d'insertion dans la table payment 
/*
INSERT INTO ecom.payments (payment_id, date, customer_id, employee_id, product_id, price) 
VALUES (300, '2024-11-02 00:00:00', 344028, 1783, 1461, 9.12);
*/



