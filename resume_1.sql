-- Найти ID с самым большим количеством заказов по годам
'1 Создаём подзапрос sq_1 ( derived table )  ->  year / an_id / cnt' ||
'2 Макс значения an_id фильтруем WHERE cnt ' ||
'3 В фильтре WHERE cnt, извлекаем сгруппированные года из подзапроса sq_1 -> HAVING to_char(ord_datetime, ''YYYY'') = sq_1.year '
SELECT *
FROM
  (SELECT to_char(ord_datetime, 'YYYY') as year, an_id, COUNT(ord_an) as cnt
  FROM analysis a
  RIGHT JOIN orders o
  ON an_id = ord_an
  GROUP BY an_id, year
  ORDER BY year) as sq_1
  WHERE cnt =
    (
      SELECT MAX(cnt)
      FROM (
        SELECT to_char(ord_datetime, 'YYYY') as year, COUNT(ord_an) as cnt
        FROM analysis a
        RIGHT JOIN orders o
        ON an_id = ord_an
        GROUP BY an_id, to_char(ord_datetime, 'YYYY')
        HAVING to_char(ord_datetime, 'YYYY') = sq_1.year
           ) as sq_2
    )
;

'/////////////////////////////////////////////'

--Рабочий
--С использованием оконной функции
'
Объяснение:
RANK() - Ранжирует Только аргумент из ORDER BY и Выполняется в Последнюю очередь
--Используется для ранжирования строк в каждой группе (по годам).
--Параметр PARTITION BY to_char(ord_datetime, ''YYYY'') делит данные на группы по годам.
--ORDER BY COUNT(ord_an) DESC упорядочивает строки по убыванию cnt в каждой группе.
WHERE rnk = 1: Так Сортировка по Убыванию, то ранжир № 1 соответствует максимальному значению COUNT(ord_an)' ||
'Оставляет только строки с максимальным значением cnt в каждом году.
ORDER BY year: Упорядочивает итоговые строки по годам.
'
SELECT year, an_id, cnt
FROM (
    SELECT
        to_char(ord_datetime, 'YYYY') AS year,
        an_id,
        COUNT(ord_an) AS cnt,
        RANK() OVER (PARTITION BY to_char(ord_datetime, 'YYYY') ORDER BY COUNT(ord_an) DESC) AS rnk
    FROM analysis a
    RIGHT JOIN orders o
    ON an_id = ord_an
    GROUP BY an_id, to_char(ord_datetime, 'YYYY')
) ranked
WHERE rnk = 1
ORDER BY year;

-- Рабочий
-- С использованием подзапроса
SELECT year, an_id, cnt
FROM (
    SELECT
        to_char(ord_datetime, 'YYYY') AS year,
        an_id,
        COUNT(ord_an) AS cnt
    FROM analysis a
    RIGHT JOIN orders o
    ON an_id = ord_an
    GROUP BY an_id, to_char(ord_datetime, 'YYYY')
) grouped
WHERE cnt = (
    SELECT MAX(cnt)
    FROM (
        SELECT
            to_char(ord_datetime, 'YYYY') AS year,
            COUNT(ord_an) AS cnt
        FROM analysis a
        RIGHT JOIN orders o
        ON an_id = ord_an
        GROUP BY to_char(ord_datetime, 'YYYY'), an_id
        HAVING to_char(ord_datetime, 'YYYY') = grouped.year
    ) yearly_max
)
ORDER BY year;



-- Исправленный вариант
WITH
  sq_1 AS (
    SELECT to_char(ord_datetime, 'YYYY') as year, an_id, COUNT(ord_an) as cnt
    FROM analysis a
    RIGHT JOIN orders o
    ON an_id = ord_an
    GROUP BY an_id, to_char(ord_datetime, 'YYYY')
  ),
  sq_2 AS (
    SELECT year, MAX(cnt) AS max_cnt
    FROM sq_1
    GROUP BY year
  )
SELECT sq_1.year, sq_1.an_id, sq_1.cnt
FROM sq_1
JOIN sq_2
ON sq_1.year = sq_2.year AND sq_1.cnt = sq_2.max_cnt
ORDER BY sq_1.year;

--////////////////////////////////////////////////////////////////////

WITH ranked_orders AS (
    SELECT
        to_char(ord_datetime, 'YYYY') as year,
        ord_an,
        RANK() OVER(PARTITION BY to_char(ord_datetime, 'YYYY')
        ORDER BY COUNT(ord_id) DESC ) as rnk
    FROM orders
    GROUP BY to_char(ord_datetime, 'YYYY'), ord_an
)
SELECT ranked_orders.year, ranked_orders.rnk
FROM  ranked_orders
WHERE rnk = 1;

--/////////////////////////////////////////////////////////////////////////////////////////

WITH
table_work as
(SELECT
   to_char(ac.date, 'MM')::FLOAT as month,
  COUNT(to_char(ac.date, 'MM')::FLOAT) as working
  FROM tinkoff.account_statuses ac
  WHERE ac.acount_status IN ('новый', 'активирован', 'утилизирован')
  GROUP BY month
ORDER BY month),
table_non_work AS
(SELECT
   to_char(ac.date, 'MM')::FLOAT as month,
  COUNT (to_char(ac.date, 'MM')::FLOAT) as non_working
  FROM tinkoff.account_statuses ac
  WHERE ac.acount_status IN ('заблокирован', 'закрыт')
  GROUP BY month
ORDER BY month)
SELECT table_work.month,
      table_work.working,
      table_non_work.non_working
FROM table_work
JOIN table_non_work
ON table_work.month = table_non_work.month
;

--////////////////////////////////////////////////////////////////////////////////////

--Нарастающим итогом рассчитать,
-- как увеличивалось количество проданных тестов каждый месяц каждого года
-- с разбивкой по группе.
-- По требованию последний столбец sum переопределён в INT
with t1 as
    (SELECT
        to_char(ord_datetime, 'YYYY') AS year,
        to_char(ord_datetime, 'MM') AS month,
        an_group,
        COUNT(ord_an)
        OVER (PARTITION BY an_group, to_char(ord_datetime, 'YYYY-MM') ORDER BY ord_datetime) AS smu_ord_an
    FROM orders
    JOIN analysis
    ON orders.ord_an = analysis.an_id),
  t2 as
    (SELECT year, month, an_group, MAX(smu_ord_an) as max_sum
      FROM t1
      GROUP BY year, month, an_group
      ORDER BY an_group, year, month)
SELECT year, month, an_group as group,
    sum(max_sum) OVER(PARTITION BY an_group, year ORDER BY month) :: int as sum
FROM t2
;

WITH t1 as(
  SELECT name,
         seat,
         LEAD(name) OVER() as ld
  FROM students
  where seat % 2 != 0
),
t2 as (
       SELECT name,
         seat,
         LAG(name) OVER() as lg
  FROM students
  where seat % 2 = 0
)


SELECT  t1.name as odd,
        t2.name as even
FROM t1
CROSS JOIN t2
WHERE t1.seat + 1 = t2.seat
;




WITH t1 as(
  SELECT name,
         seat,
         LEAD(name) OVER() as ld
  FROM students
  where seat % 2 != 0
),
t2 as (
       SELECT name,
         seat,
         LAG(name) OVER() as lg
  FROM students
  where seat % 2 = 0
)
SELECT
t1.seat as st1,
t1.name as odd,
t2.seat as st2,
        t2.name as even
FROM t1
CROSS JOIN t2
WHERE t1.seat + 1 = t2.seat
;

-- //////////////////////////////////////////////////////////////
--Требуется вывести уникальное количество людей из города “Москва”,
-- которые купили “Телефон” в сентябре и октябре.
select month, SUM(cnt :: int) as cnt_people
from  (SELECT to_char(p.created_at, 'Month') as month,
        city,
        COUNT(user_id) as cnt
    FROM ozon.users u
    RIGHT JOIN ozon.purchases p
    ON u.id = p.user_id
    WHERE to_char(p.created_at, 'MM') in ('09','10') and city = 'Москва'
    GROUP BY city, month, user_id
    HAVING COUNT(user_id) = 1) as t1
GROUP BY month
ORDER by cnt_people DESC
;

--//////////////////////////////////////////////////////////////
--Для каждого анализа вывести: ID анализа, кол-во продаж
--за 2019 год и кол-во продаж за 2020 год.
-- Столбцы по условию year2019 и year2020
-- Транспонируем таблицу, строки 2019 и 2020 в столбцы year2019 и year2020

select an,
-- Создаём столбцы year2019 и year2020 и помещаем значения с инф о количестве проданных анализов
    MAX(CASE
        WHEN dt = '2019' THEN cnt_ord
        ELSE NULL
        END ) AS year2019,
     MAX(CASE
        WHEN dt = '2020'  THEN cnt_ord
        ELSE NULL
        END ) AS year2020
-- Подзапрос где джойним таблицу заказов с таблицей справочником инф по анализам
from    (SELECT
        an.an_id as an,
        to_char(ord_datetime, 'YYYY') as dt,
        COUNT(ord_an)  as cnt_ord
    FROM orders o
    JOIN analysis an
    on an_id = ord_an
    WHERE to_char(ord_datetime, 'YYYY') in ('2019', '2020')
    GROUP BY dt, an.an_id
    ORDER BY dt) as t1
-- Группировка по id анализов обязательна иначе в столбцах будет NULL
GROUP BY an
ORDER BY an
;

--////////////////////////////////////////////////////////////////////////
--Выведите следующую информацию:
--ID анализа
--количество продаж каждого анализа в штуках с 01.03.2019 по 01.03.2020 (включительно обе даты)
--группа продаж по количеству продаж каждого анализа

SELECT an_id,
        amount,
        CASE        -- CASE используем с and
            WHEN amount > 40 THEN 2
            WHEN amount > 30 AND amount <= 40 THEN 1
            WHEN amount <= 30  THEN 0
            ELSE 0
         END gr
FROM
    (SELECT
        an_id,
        COUNT (ord_an) as amount
    FROM orders
    LEFT JOIN analysis
    ON an_id = ord_an
    WHERE ord_datetime BETWEEN '2019-03-01' AND '2020-03-01'
    GROUP BY  an_id
    ORDER BY an_id) as t1
;

SELECT an_id,
        amount,
        CASE     -- CASE используем с BETWEEN
            WHEN amount > 40 THEN 2
            WHEN amount BETWEEN  30 AND 40 THEN 1
            WHEN amount <= 30  THEN 0
            ELSE 0
         END gr
FROM
    (SELECT
        an_id,
        COUNT (ord_an) as amount
    FROM orders
    LEFT JOIN analysis
    ON an_id = ord_an
    WHERE ord_datetime BETWEEN '2019-03-01' AND '2020-03-01'
    GROUP BY  an_id
    ORDER BY an_id) as t1
;

-- Необходимо вывести количество людей из Тулы, которые покупали телефоны с разбивкой по месяцам.
-- Примечание. Телефоны - это товары с категорей 2 из таблицы skus.
-- DISTINCT - Если один человек купил несколько раз за месяц, считаем это за одну покупку.
-- Важно: Месяца должны быть представлены не в виде цифр, а в виде английских слов с нижнем регистром.
-- Важно: Обратите внимание, что название столбцов в вашем ответе должно в точности совпадать с условием.
-- Результат должен быть отсортирован по убыванию значений в столбце people
 select LOWER(mn) as month,
         COUNT(DISTINCT(id_customer)) as people
   FROM customer c
   RIGHT JOIN
            (SELECT user_id,
                     to_char(created_at, 'Month') as mn,
                     sku_id
             FROM purchases p
             LEFT join skus s
             on s.id = p.sku_id
             WHERE category = 2) as cat
    ON cat.user_id = c.id_customer
    WHERE town = 'Tula'
    GROUP BY month
    ORDER BY people DESC
;

-- Необходимо вывести сотрудников и дни, когда они находились на рабочем месте менее 8 часов.
SELECT employee,
       check_time,
       is_entered
from gate
;
-- из GPT
SELECT
    EXTRACT(epoch FROM (end_time - start_time)) / 3600 AS hours,
    EXTRACT(epoch FROM (end_time - start_time)) / 60 AS minutes
FROM
    (SELECT '2020-11-25 08:00:00'::timestamp AS start_time,
            '2020-11-25 15:59:00'::timestamp AS end_time) AS event;
