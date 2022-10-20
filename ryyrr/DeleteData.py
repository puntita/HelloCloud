@app.route('/product/<id>', methods=['DELETE'])
def update_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)