from unicodedata import name
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from matplotlib.pyplot import cla
from numpy import product
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_ker=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty =qty

class ProductSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'description', 'price', 'qty')


product_schema = ProductSchema()
product_schema = ProductSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)