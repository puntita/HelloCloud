@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = product_schema.dump(all_products)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)