Query 1: Total spending per customer
SELECT
    customer_id,
    name,
    SUM(amount) AS total_spending
FROM customer_order_report
GROUP BY customer_id, name
ORDER BY total_spending DESC;


Query 2: Find repeat customers
SELECT
    customer_id,
    name,
    COUNT(*) AS total_orders
FROM customer_order_report
GROUP BY customer_id, name
HAVING COUNT(*) > 1
ORDER BY total_orders DESC;


Query 3: Find customers who have never placed an order
SELECT
    c.customer_id,
    c.name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;