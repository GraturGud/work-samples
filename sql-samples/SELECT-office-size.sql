/*Listing all company offices and specifying their ID, country, city, phone N and the amount of employees working there*/
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