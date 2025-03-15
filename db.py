from tinydb import TinyDB, Query


class ProductsDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        self.table = self.db.table('Products')
    
    def all_products(self):         #1
        """Returns all products in the database"""
        return self.table.all()
    
    def get_product_id(self, id):     #2
        """Returns all products by id"""
        return self.table.search(self.query.id == id)
    
    def get_all_product_names(self):    #3
        """Returns all product names"""
        return [product['name'] for product in self.table.all() if 'name' in product]

    def get_names(self, name: str):      #4
        """Returns all products by name"""
        return self.table.search(self.query.name == name)

    def get_all_catagories(self):       #5
        """Returns all catagories name"""
        return [product['category'] for product in self.table.all() if 'category' in product]
    
    def get_small_from_price(self, price):    #6
        """Returns products if product's price small from price"""
        return self.table.search(self.query.price < price)

    def expensive_products(self):     #7
        """Returns a top three expensive products"""
        return self.table.search(self.query.price[::-3])
    
    def get_between_price(self, max_price, min_price):     #8
        """Returns a products between max_price and min_price"""
        return self.table.search((self.query.price >= min_price) & (self.query.price <= max_price))

    def add_product(self, product):    #9
        """Adds a product to the database"""
        return self.table.insert(product)

    def delete_product(self, doc_id):    #10
        """Deletes a product from the database"""
        return self.table.remove(doc_ids=[doc_id])
