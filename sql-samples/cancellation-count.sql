/*Вывод наименований и линейки продуктов с указанием кол-ва на складе и кол-ва отмен*/
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
    WHERE orders.status='Cancelled'
    GROUP BY prodName, prodLine, numInStock
    ORDER BY prodLine, numCancelled DESC;