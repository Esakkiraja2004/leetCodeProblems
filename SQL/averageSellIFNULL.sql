-- # Write your MySQL query statement below
SELECT P.product_id , IFNULL(ROUND(SUM(U.units*P.price) / sum(U.units) , 2),0) AS average_price
FROM Prices P
LEFT JOIN UnitsSold U
ON IFNULL(P.product_id = U.product_id, 0) AND U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY P.product_id
