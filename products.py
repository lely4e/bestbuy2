class NonStockedProduct:
    def __init__(self, name, price):
        """Initialize a product"""
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.active = True
        self.name = name
        self.price = price
        self.promotion = None

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promo):
        self.promotion = promo

    def is_active(self) -> bool:
        """Return True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activate the product"""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def show(self):
        """Display the product"""
        print(f"{self.name}, Price: {self.price}")  # , Promotion: {self.promotion}

    def buy(self, amount) -> float:
        """Buy a quantity of the product"""
        if amount <= 0:
            raise ValueError("Quantity must be a positive number")

        # Returns the total price (float) of the purchase
        return self.price * amount


class Product(NonStockedProduct):
    """A class to represent a product, it's name, price, quantity and status"""

    def __init__(self, name, price, quantity):
        """Initialize a product"""
        super().__init__(name, price)

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

    def get_quantity(self) -> int:
        """Return the quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity of the product"""
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a number")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def show(self):
        """Display the product"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, amount) -> float:
        """Buy a quantity of the product"""
        # Check if there are enough quantity
        total_price = super().buy(amount)

        if amount > self.quantity:
            raise ValueError(
                "Error while making order! Quantity larger than what exists"
            )
        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, amount)
        # Updates the quantity of the product
        self.quantity -= amount

        # Check how many items left in stock
        if self.quantity == 0:
            self.deactivate()

        # Returns the total price (float) of the purchase
        return total_price


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum=1):
        """Initialize a product"""

        super().__init__(name, price, quantity)

        if maximum <= 0:
            raise ValueError("It can not be lower than 0")

        self.maximum = maximum

    def show(self):
        """Display the product"""
        print(
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"
        )

    def buy(self, amount) -> float:
        """Buy a quantity of the product"""
        # Check if there are enough quantity

        if amount > self.maximum:
            raise ValueError(f"You can buy it only {self.maximum} times")

        return super().buy(amount)


# product = NonStockedProduct("MacBook", 1450)
# product1 = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
# tester = LimitedProduct("Tester", price=0, quantity=250, maximum=3)
# # print(product.show())
# # print(product.buy())
# print(product1.show())
# print(tester.buy(4))
# print(product1.buy(1))
