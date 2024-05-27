CREATE DATABASE sales_db;
-- Use the sales_db database
USE sales_db;

-- Create Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255)
);

-- Create Products table
CREATE TABLE IF NOT EXISTS Products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Create Orders table
CREATE TABLE IF NOT EXISTS Orders (
    order_id VARCHAR(10) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(10),
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create OrderItems table
CREATE TABLE IF NOT EXISTS OrderItems (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(10),
    product_id VARCHAR(10),
    quantity INT,
    price DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Show all tables in the database
SHOW TABLES;

-- Describe each table
DESCRIBE Customers;
DESCRIBE Products;
DESCRIBE Orders;
DESCRIBE OrderItems;
