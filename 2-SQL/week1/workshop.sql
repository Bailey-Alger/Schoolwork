-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY(id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);


-- TODO create more tables here...

CREATE TABLE suppliers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customers (
    customer_id SERIAL,
    company_name TEXT NOT NULL,
    PRIMARY KEY (customer_id)
);

CREATE TABLE employees (
    employee_id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY (employee_id),
    territory_id INT NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL,
    date DATE,
    PRIMARY KEY (order_id),
    employee_id INT UNIQUE,
    customer_id INT NOT NULL UNIQUE
);

CREATE TABLE orders_products (
    quantity INT NOT NULL,
    discount NUMERIC NOT NULL
);

CREATE TABLE territories (
    territory_id SERIAL,
    description TEXT,
    PRIMARY KEY (territory_id)
);

CREATE TABLE employees_territories (
    id SERIAL,
    PRIMARY KEY (id)
);

CREATE TABLE offices (
    id SERIAL,
    address_line TEXT,
    PRIMARY KEY (ID),
    territory_id INT NOT NULL UNIQUE
);

CREATE TABLE us_states (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    abbreviation CHARACTER(2) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

---
--- Add foreign key constraints
---

ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories;
       
-- TODO create more constraints here...

ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY(customer_id)
REFERENCES customers;

ALTER TABLE orders
ADD CONSTRAINT fk_employee
FOREIGN KEY(employee_id)
REFERENCES employees;

ALTER TABLE offices
ADD CONSTRAINT fk_territories
FOREIGN KEY (territory_id)
REFERENCES territories