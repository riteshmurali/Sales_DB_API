from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.String(10), primary_key=True)
    customer_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(255))

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.String(10), primary_key=True)
    product_name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2))

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.String(10), primary_key=True)
    order_date = db.Column(db.Date)
    customer_id = db.Column(db.String(10), db.ForeignKey('customers.customer_id'))
    total_amount = db.Column(db.Numeric(10, 2))

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.String(10), db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.String(10), db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Numeric(10, 2))
    total_price = db.Column(db.Numeric(10, 2))
