/*Вывод всех офисов с указанием ID, страны, города, телефона и кол-вом сотрудников*/
SELECT 
    offices.officeCode AS officeCode,
    offices.country AS officeCountry,
    offices.city AS officeCity,
    offices.phone AS phoneNum,
    COUNT(employees.employeeNumber) AS numEmployees
FROM
    offices
        INNER JOIN
    employees ON offices.officeCode = employees.officeCode
GROUP BY officeCode , officeCountry , officeCity , phoneNum
ORDER BY numEmployees DESC;