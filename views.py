from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from config import Config
from models import db, Customer, Product, Order, OrderItem
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


def get_top_products(query, params, n):
    results = db.session.execute(query, params).fetchall()
    return [{'product_id': row[0], 'product_name': row[1], 'total_quantity': row[2]} for row in results][:n]

@app.route('/api/top-products/overall', methods=['GET'])
def top_products_overall():
    n = int(request.args.get('n', 5))
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Please provide both start_date and end_date"}), 400
    
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Date format should be YYYY-MM-DD"}), 400
    
    query = text("""
    SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity
    FROM products p
    JOIN OrderItems oi ON p.product_id = oi.product_id
    JOIN orders o ON oi.order_id = o.order_id
    WHERE o.order_date BETWEEN :start_date AND :end_date
    GROUP BY p.product_id, p.product_name
    ORDER BY total_quantity DESC
    """)
    
    params = {'start_date': start_date, 'end_date': end_date}
    return jsonify(get_top_products(query, params, n))

@app.route('/api/top-products/category', methods=['GET'])
def top_products_by_category():
    n = int(request.args.get('n', 5))
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date or not category:
        return jsonify({"error": "Please provide category, start_date, and end_date"}), 400
    
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Date format should be YYYY-MM-DD"}), 400
    
    query = text("""
    SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity
    FROM products p
    JOIN OrderItems oi ON p.product_id = oi.product_id
    JOIN orders o ON oi.order_id = o.order_id
    WHERE p.category = :category AND o.order_date BETWEEN :start_date AND :end_date
    GROUP BY p.product_id, p.product_name
    ORDER BY total_quantity DESC
    """)
    
    params = {'category': category, 'start_date': start_date, 'end_date': end_date}
    return jsonify(get_top_products(query, params, n))

@app.route('/api/top-products/region', methods=['GET'])
def top_products_by_region():
    n = int(request.args.get('n', 5))
    region = request.args.get('region')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date or not region:
        return jsonify({"error": "Please provide region, start_date, and end_date"}), 400
    
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Date format should be YYYY-MM-DD"}), 400
    
    query = text("""
    SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity
    FROM products p
    JOIN OrderItems oi ON p.product_id = oi.product_id
    JOIN orders o ON oi.order_id = o.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE c.address LIKE :region AND o.order_date BETWEEN :start_date AND :end_date
    GROUP BY p.product_id, p.product_name
    ORDER BY total_quantity DESC
    """)
    
    params = {'region': f'%{region}%', 'start_date': start_date, 'end_date': end_date}
    return jsonify(get_top_products(query, params, n))



if __name__ == '__main__':
    app.run(debug=True)
