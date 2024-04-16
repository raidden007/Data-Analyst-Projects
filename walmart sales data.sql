CREATE DATABASE IF NOT EXISTS salesDataWalmart;

CREATE TABLE IF NOT EXISTS sales(
	invoice_id VARCHAR(30) NOT NULL PRIMARY KEY,
    branch VARCHAR(5) NOT NULL,
    city VARCHAR(30) NOT NULL,
    customer_type VARCHAR(30) NOT NULL,
    gender VARCHAR(30) NOT NULL,
    product_line VARCHAR(100) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    tax_pct FLOAT(6,4) NOT NULL,
    total DECIMAL(12, 4) NOT NULL,
    date DATETIME NOT NULL,
    time TIME NOT NULL,
    payment VARCHAR(15) NOT NULL,
    cogs DECIMAL(10,2) NOT NULL,
    gross_margin_pct FLOAT(11,9),
    gross_income DECIMAL(12, 4),
    rating FLOAT(2, 1)
);

SELECT *
FROM salesDataWalmart.sales;

--------------------------------------------------------------------------------------------------
----------------------------------------Feature Engineering --------------------------------------

--- time_of_day

SELECT 
    time,
    CASE 
        WHEN time BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
        WHEN time BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END AS time_of_day
FROM sales;

ALTER TABLE salesDataWalmart.sales ADD COLUMN time_of_day VARCHAR(20);

UPDATE salesDataWalmart.sales
SET time_of_day = (
        CASE 
        WHEN time BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
        WHEN time BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END
);

-- day_name

SELECT date,
DAYNAME(date) AS day_name
FROM sales;

ALTER TABLE salesDataWalmart.sales ADD COLUMN day_name VARCHAR(10);

UPDATE salesDataWalmart.sales
SET day_name = DAYNAME(date);



-- month_name

SELECT date,
MONTHNAME(date)
FROM sales;


ALTER TABLE salesDataWalmart.sales ADD COLUMN month_name VARCHAR(10);

UPDATE salesDataWalmart.sales
SET month_name = MONTHNAME(date);


---------------------------------------------------------------------------------
--------------------------- Questions to answer ---------------------------------

--- How many unique cities does the data have?
SELECT 
DISTINCT city
FROM salesDataWalmart.sales;

-- In which city is each branch?
SELECT 
DISTINCT branch
FROM salesDataWalmart.sales;

SELECT 
DISTINCT city,
branch
FROM salesDataWalmart.sales;


------------ Product -------------------------

--- How many unique product lines does the data have?
SELECT COUNT(DISTINCT product_line)
FROM sales;

--- What is the most common payment method?
SELECT payment_method, 
COUNT(payment_method) AS cnt
FROM sales
GROUP BY payment_method
ORDER BY cnt DESC;

--- What is the most selling product line?
SELECT product_line, 
COUNT(product_line) AS cnt
FROM sales
GROUP BY product_line
ORDER BY cnt DESC;

--- What is the total revenue by month?
SELECT month_name AS month,
SUM(total) AS total_revenue
FROM salesDataWalmart.sales
GROUP BY month_name
ORDER BY total_revenue DESC;

--- What month had the largest COGS?
SELECT month_name AS month,
SUM(cogs) AS cogs
FROM sales
GROUP BY month_name
ORDER BY cogs DESC;


--- What product line had the largest revenue?
SELECT product_line,
SUM(total) AS total_revenue
FROM sales
GROUP BY product_line
ORDER BY total_revenue DESC;














     