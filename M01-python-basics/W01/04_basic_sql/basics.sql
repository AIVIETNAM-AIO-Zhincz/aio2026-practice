-- AIO2026 M01W01 - Basic SQL (PostgreSQL) — 04/06/2026
-- CREATE / INSERT / SELECT / WHERE / JOIN

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    state       VARCHAR(2),
    points      INT
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date  DATE
);

INSERT INTO customers (customer_id, first_name, last_name, state, points) VALUES
    (1, 'Babara', 'MacCaffrey', 'MA', 2273),
    (2, 'Ines',   'Brushfield', 'VA', 947),
    (3, 'Freddi', 'Boagey',     'CO', 2967);

-- Lọc + sắp xếp + giới hạn
SELECT * FROM customers WHERE points > 1000 ORDER BY points DESC LIMIT 2;

-- IN / BETWEEN
SELECT * FROM customers WHERE state IN ('VA', 'CO') AND points BETWEEN 500 AND 3000;

-- JOIN hai bảng qua khoá chung
SELECT c.first_name, c.last_name, o.order_id, o.order_date
FROM customers AS c
JOIN orders   AS o ON c.customer_id = o.customer_id;

-- PostgreSQL: phân trang dùng LIMIT ... OFFSET, regex dùng toán tử ~
SELECT * FROM customers ORDER BY points DESC LIMIT 2 OFFSET 1;
SELECT * FROM customers WHERE last_name ~ 'ey$';
