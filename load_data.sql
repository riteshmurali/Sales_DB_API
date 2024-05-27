-- Use the sales_db database
USE sales_db;

-- Insert data into Customers table
INSERT INTO Customers (customer_id, customer_name, email, address) VALUES
('C456', 'John Smith', 'johnsmith@email.com', '123 Main St, Anytown, CA 12345'),
('C789', 'Emily Davis', 'emilydavis@email.com', '456 Elm St, Otherville, NY 54321'),
('C101', 'Sarah Johnson', 'sarahjohnson@email.com', '789 Oak St, New City, TX 75024');

-- Insert data into Products table
INSERT INTO Products (product_id, product_name, category, price) VALUES
('P123', 'UltraBoost Running Shoes', 'Shoes', 180.00),
('P456', 'iPhone 15 Pro', 'Electronics', 1299.00),
('P789', 'Levi\'s 501 Jeans', 'Clothing', 59.99),
('P234', 'Sony WH-1000XM5 Headphones', 'Electronics', 349.99);

-- Insert data into Orders table
INSERT INTO Orders (order_id, order_date, customer_id, total_amount) VALUES
('1001', '2023-12-15', 'C456', 2 * 180.00 * (1 - 0.1) + 10.00),
('1002', '2024-01-03', 'C789', 1 * 1299.00 * (1 - 0.0) + 15.00),
('1003', '2024-02-28', 'C456', 3 * 59.99 * (1 - 0.2) + 5.00),
('1004', '2024-03-10', 'C101', 1 * 180.00 * (1 - 0.0) + 8.00),
('1005', '2024-04-22', 'C789', 1 * 349.99 * (1 - 0.15) + 12.00),
('1006', '2024-05-18', 'C101', 2 * 1299.00 * (1 - 0.05) + 20.00);

-- Insert data into OrderItems table
INSERT INTO OrderItems (order_id, product_id, quantity, price, total_price) VALUES
('1001', 'P123', 2, 180.00, 2 * 180.00 * (1 - 0.1)),
('1002', 'P456', 1, 1299.00, 1 * 1299.00 * (1 - 0.0)),
('1003', 'P789', 3, 59.99, 3 * 59.99 * (1 - 0.2)),
('1004', 'P123', 1, 180.00, 1 * 180.00 * (1 - 0.0)),
('1005', 'P234', 1, 349.99, 1 * 349.99 * (1 - 0.15)),
('1006', 'P456', 2, 1299.00, 2 * 1299.00 * (1 - 0.05));
