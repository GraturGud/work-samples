/*Есть таблица wi_users в схеме APEX. В данной таблице есть следующие колонки:
•	wi_usr_surname – Фамилия
•	wi_usr_phone – Телефон
•	wi_usr_last_act_dt – Последняя дата входа в приложение
Задачи:

•	Написать запрос с выводом количества уникальных по фамилии зарегистрированных пользователей с 01.07.2021*/
SELECT COUNT(DISTINCT wi_usr_surname) as num_users
FROM wi_users
WHERE wi_usr_last_act_dt >= '2021-07-01';
/*•	Написать запрос для поиска количества пользователей с номером телефона, оканчивающегося на 9798*/
SELECT COUNT(*) as num_users
FROM wi_users
WHERE wi_usr_phone LIKE '%9798';
/*•	Написать запрос с выводом зарегистрированных пользователей c 01.07.2021, отсортированных по фамилии в обратном алфавитном порядке*/
SELECT *
FROM wi_users
WHERE wi_usr_last_act_dt >= '2021-07-01'
ORDER BY wi_usr_surname DESC;
