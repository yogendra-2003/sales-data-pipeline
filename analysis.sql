# A. Calculate total revenue by product
SELECT
    product,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;



#B. Find total sales by month
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    SUM(quantity * price) AS monthly_revenue
FROM sales
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;


C. Find the number of orders for each product
SELECT
    product,
    COUNT(*) AS order_count
FROM sales
GROUP BY product;