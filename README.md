Steps to Execute:

Create the database on any server. ( I used MySQLWorkBench),

Run create_tables.sql. This will create the schema and required tables.

Run load_data.sql. this will load the sample data.

create, save, and run. app.py, config.py, models.py and views.py.

my API urls:
http://127.0.0.1:5000/api/top-products/overall?n=4&start_date=2023-12-15&end_date=2024-12-31
http://127.0.0.1:5000/api/top-products/category?category=electronics&start_date=2023-12-15&end_date=2024-12-31
http://127.0.0.1:5000/api/top-products/region?n=5&start_date=2023-12-15&end_date=2024-12-31&region=123%20Main%20St,%20Anytown,%20CA%2012345
