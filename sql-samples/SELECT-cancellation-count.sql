/*Counting the amount of cancellations for a product and specifying each listed product's product line and amount in stock*/
SELECT 
    products.productName AS prodName,
    products.productLine AS prodLine,
    products.quantityInStock AS numInStock,
    COUNT(orders.orderNumber) AS numCancelled
FROM
    products
        INNER JOIN
    orderdetails ON products.productCode = orderdetails.productCode
        INNER JOIN
    orders ON orderdetails.orderNumber = orders.orderNumber
WHERE
    orders.status = 'Cancelled'
GROUP BY prodName , prodLine , numInStock
ORDER BY prodLine , numCancelled DESC;