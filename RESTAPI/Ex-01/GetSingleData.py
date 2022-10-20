from numpy import product


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)