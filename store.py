import products


class Store:
    """A class to store products"""

    def __init__(self, products_list):
        """Initialize a product"""
        self.products = products_list

    def add_product(self, product):
        """Add a product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of the product in the store"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """Return a list of all products in the store"""
        return self.products

    @staticmethod
    def order(shopping_list) -> float:
        """Order the product in the store"""
        # Gets a list of tuples: Product (Product class) and quantity (int)
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
