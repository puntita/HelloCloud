from crypt import methods
from distutils.log import debug

from flask import request
from numpy import product


@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add = Product(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


if __name__ == '__main__':
    app.run(debug=True)