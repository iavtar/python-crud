from dao.product_dao import ProductDao

class ProductService:

    def __init__(self):
        self.dao = ProductDao()

    def add_product(self, product):
        return self.dao.insert(product)