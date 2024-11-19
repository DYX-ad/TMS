1. Создание таблицы "Employees"

CREATE TABLE Employees ( Name VARCHAR(100), 
Position VARCHAR(50), 
Department VARCHAR(50), 
Salary NUMERIC(10, 2) );

2. Вставка нескольких записей в таблицу

INSERT INTO Employees (Name, Position, Department, Salary) VALUES 
('Alice Johnson', 'Developer', 'IT', 4500), 
('Bob Smith', 'Manager', 'Sales', 6500), 
('Carol White', 'Analyst', 'Finance', 5200), 
('David Brown', 'Developer', 'IT', 4800), 
('Eve Black', 'Manager', 'HR', 6000);

3. Изменение данных: изменение должности одного из сотрудников

UPDATE Employees 
SET Position = 'Senior Developer' 
WHERE Name = 'Alice Johnson';

4. Добавление нового поля "HireDate" (дата приема на работу)

ALTER TABLE Employees 
ADD COLUMN HireDate DATE;

5. Добавление даты приема на работу для всех сотрудников

UPDATE Employees 
SET HireDate = '2020-05-10' 
WHERE Name = 'Alice Johnson'; 

UPDATE Employees 
SET HireDate = '2019-03-22'
 WHERE Name = 'Bob Smith'; 

UPDATE Employees 
SET HireDate = '2018-11-15' 
WHERE Name = 'Carol White'; 

UPDATE Employees 
SET HireDate = '2021-02-01'
 WHERE Name = 'David Brown'; 

UPDATE Employees 
SET HireDate = '2017-07-19'
 WHERE Name = 'Eve Black';

6-9. Функция для поиска по условиям (по должности, по з/п выше определенной суммы, по отделу)

CREATE OR REPLACE FUNCTION get_employee_data( 
            job_title VARCHAR(50) DEFAULT NULL, 
            min_salary NUMERIC(10, 2) DEFAULT NULL, 
            dept_name VARCHAR(50) DEFAULT NULL )

 RETURNS TABLE (Name VARCHAR, Position VARCHAR, Department VARCHAR, S
alary NUMERIC, HireDate DATE) AS $$ 
BEGIN 
           RETURN QUERY 
           SELECT Name, Position, Department, Salary, HireDate 
           FROM Employees 
           WHERE 
                      (job_title IS NULL OR Position = job_title) AND 
                      (min_salary IS NULL OR Salary > min_salary) AND 
                      (dept_name IS NULL OR Department = dept_name); 
END; $$ 
LANGUAGE plpgsql;

10. Удаление таблицы "Employees"

DROP TABLE Employees;
