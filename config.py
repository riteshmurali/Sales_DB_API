import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/sales_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
