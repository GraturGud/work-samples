/*Listing employees having a managerial position and specifying the amount of people reporting directly to them*/
SELECT 
    m.firstName AS bossFirstname,
    m.lastName AS bossLastName,
    m.jobTitle AS bossJobTitle,
    SUM(IF(m.employeeNumber IN (SELECT 
                reportsTo
            FROM
                employees),
        1,
        0)) AS numEmployees
FROM
    employees m
        RIGHT JOIN
    employees e ON e.reportsTo = m.employeeNumber
WHERE
    m.employeeNumber IS NOT NULL
GROUP BY m.firstName , m.lastName , m.jobTitle;