from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"mensaje": "ppong"})

@app.route('/products')
def getProducts():
    return jsonify({"message": "List of products","products": products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        return jsonify({'producto': productsFound[0]})
    return jsonify({'message': 'product not found'})

@app.route('/products', methods=['POST'])
def addProduct():
    newProduct = {
        "name": request.json['name'], 
        "price":request.json['price'] , 
        "quantity": request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({"message": "product added succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound= [product for product in products if product['name']==product_name]
    if len(productsFound)>0:
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['rpice'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productsFound[0]
        })
    return jsonify({"message": "product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name']== product_name]
    if len(productsFound)>0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "product deleted",
            "product": products
        })
    return jsonify({
        "message": "product not found"
    })




if __name__ == '__main__':
    app.run(debug=True, port=4000)