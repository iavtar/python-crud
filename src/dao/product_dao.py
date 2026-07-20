from config.db import getConnection
from model.product import Product

class ProductDao:

    def insert(self, product):
        connection = getConnection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO products(name, price, quantity)
            VALUES(%s, %s, %s)
        """
        cursor.execute(
            sql,
            (
                product.name,
                product.price,
                product.quantity
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
