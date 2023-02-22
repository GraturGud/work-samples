/*Listing employees' names and positions, specifying if they have a managerial position and providing information about their bosses*/
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