from service.product_service import ProductService
from model.product import Product

service = ProductService()

def menu():
    print("""
    1- Add Product
    2- Update Product
    3- Find Product
    4- Delete Product
    5- Exit
    """)
    return int(input("Enter Choice : "))

while True:
    choice = menu()

    if choice == 1:
        name = input("Name: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        product = Product(name=name, price=price, quantity=quantity)
        service.add_product(product)
        print("Product Added!")