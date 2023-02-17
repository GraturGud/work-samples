/*Вывод имен и должностей сотрудников, сведения о том имеют ли они подчиненных, имена и должности их прямых начальников*/
SELECT 
    e.firstName AS empFirstname,
    e.lastName AS empLastName,
    e.jobTitle AS empJobTitle,
    IF(e.employeeNumber IN (SELECT 
                reportsTo
            FROM
                employees),
        'YES',
        'NO') AS isManager,
    m.firstName AS bossFirstName,
    m.lastName AS bossLastName,
    m.jobTitle AS bossJobTitle
FROM
    employees e
        LEFT JOIN
    employees m ON e.reportsTo = m.employeeNumber
ORDER BY isManager DESC , m.firstName , e.firstName;