/*Вывод id покупателя, наименование покупателя, подсчет доставленных заказов, заказов в пути, отмененных заказов, удержанных заказов, оспариваемых заказов и решенных заказов*/
SELECT 
    customers.customerNumber,
    customers.customerName,
    SUM(IF(orders.status = 'Shipped', 1, 0)) AS numShipped,
    SUM(IF(orders.status = 'In Process', 1, 0)) AS numInProcess,
    SUM(IF(orders.status = 'Cancelled', 1, 0)) AS numCancelled,
    SUM(IF(orders.status = 'On Hold', 1, 0)) AS numOnHold,
    SUM(IF(orders.status = 'Disputed', 1, 0)) AS numDisputed,
    SUM(IF(orders.status = 'Resolved', 1, 0)) AS numResolved
FROM
    customers
        INNER JOIN
    orders ON customers.customerNumber = orders.customerNumber
WHERE
    orders.status IN ('In Process' , 'Shipped',
        'On Hold',
        'Cancelled',
        'Disputed',
        'Resolved')
GROUP BY customers.customerNumber , customers.customerName
ORDER BY numShipped DESC , numInProcess DESC , numCancelled DESC;