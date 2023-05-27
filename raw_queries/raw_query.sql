-- Query that utilizes temporary tables with unnecessary columns

-- Create a temporary table to store orders
CREATE OR REPLACE TEMPORARY TABLE temp_orders AS
SELECT name, date
FROM orders;

-- Create a temporary table to store customers
CREATE OR REPLACE TEMPORARY TABLE temp_customers AS
SELECT *
FROM customers;

-- Query to retrieve order details with unnecessary customer information
WITH temp_orders_with_customers AS (
  SELECT o.order_id, o.order_date, o.total_amount, c.*
  FROM temp_orders o
  JOIN temp_customers c ON o.customer_id = c.customer_id;
)
SELECT *
FROM temp_orders_with_customers;
