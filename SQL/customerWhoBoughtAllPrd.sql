-- # Write your MySQL query statement below

SELECT C.customer_id FROM Customer C
JOIN Product P
ON P.product_key = C.product_key 
GROUP BY C.customer_id
HAVING COUNT(DISTINCT P.product_key) = (SELECT COUNT(product_key) FROM Product);