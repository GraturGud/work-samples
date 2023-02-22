/*Creates a table with the list of cancelled orders with order details included*/
CREATE TABLE cancelled AS (SELECT o.orderNumber,
    o.orderDate,
    o.requiredDate,
    o.shippedDate,
    o.status,
    o.comments,
    o.customerNumber,
    d.productCode,
    d.quantityOrdered,
    d.priceEach,
    d.orderLineNumber FROM
    orders o
        INNER JOIN
    orderdetails d ON o.orderNumber = d.orderNumber
WHERE
    status = 'Cancelled'
ORDER BY o.orderNumber);