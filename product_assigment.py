from abc import ABC, abstractmethod


class Product:

    product_name = ""
    product_size = ""
    expiry_date = ""
    manufacture_date = ""
    product_colour = ""
    product_number = ""


class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass


class ProductManager(ProductAbstract):

    def create_product(self, product: Product):
        print("Create a new product here")
        print(f"Product name : {product.product_name}")

    def edit_product(self, product: Product):
        print("Please wait to edit product")
        print(f"Current product number to be edited: {product.product_number}")

    def get_product_by_id(self):
        print("Scan to see product ID..")

    def get_all_products(self):
        print("Finding all products, please wait...")

    def upload_product_image(self):
        print("Show product image")

    def delete_product(self):
        print("Delete this product")
