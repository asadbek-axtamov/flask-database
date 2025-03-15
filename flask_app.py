from flask import Flask, request
from db import ProductsDB


app = Flask(__name__)
db = ProductsDB('products_db.json')

## view all products
@app.route('/products', methods=['GET'])
def get_all_products():            #1+
    """Returns all products in the database"""
    return db.all_products() 

# view all product by id
@app.route('/products/id/<int:id>', methods=['GET'])
def get_all_product(id):         #2+
    """Returns product in the database by id"""
    return db.get_product_id(id)

# view all ptoducts names
@app.route('/products/names', methods=['GET'])
def get_product_all_names():      #3+
    """Returns all product names"""
    return db.get_all_product_names()


# view products by name
@app.route('/products/name/<name>', methods=['GET'])
def get_products_by_name(name):            #4+
    """Returns a product by name"""
    return db.get_names(name)

# view all ptoducts catagories
@app.route('/products/catagories', methods=['GET'])
def get_product_all_catagories():            #5+
    """Returns all product catagories"""
    return db.get_all_catagories()

# view products by price
@app.route('/products/price/<int:price>', methods=['GET'])
def get_products_by_price(price):        #6+
    """Returns a product by price"""
    return db.get_small_from_price(price)

# view products expensive
@app.route('/products/price/top/expensive', methods=['GET'])
def get_products_expensive():        #7  price
    """Returns a top three expensive products"""
    return db.expensive_products()

# view products between max_price and min_price
@app.route('/products/price/between', methods=['GET'])
def get_between_price():        #8
    """Returns a products between max_price and min_price
    get max_price and min_price from query_string
    """
    return db.get_between_price()

# view add product
@app.route('/products/add', methods=['POST'])
def add_products():          #9
    """Adds a product to the database"""
    return db.add_product()


# view delete product
@app.route('/products/delete/<doc_id>', methods=['DELETE'])
def delete_product(doc_id):      #10
    """Deletes a product from the database"""
    return db.delete_product(doc_id)



if __name__ == '__main__':
    app.run(debug=True)