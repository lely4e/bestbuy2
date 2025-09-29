class Product:
    """A class to represent a product, it's name, price, quantity and status"""

    def __init__(self, name, price, quantity):
        """Initialize a product"""
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.active = True
        self.name = name
        self.price = price
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
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buy a quantity of the product"""
        # Check if there are enough quantity
        if quantity > self.quantity:
            raise ValueError(
                "Error while making order! Quantity larger than what exists"
            )
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number")

        # Buys a given quantity of the product
        total_price = self.price * quantity

        # Updates the quantity of the product
        self.quantity -= quantity

        # Check how many items left in stock
        if self.quantity == 0:
            self.deactivate()

        # Returns the total price (float) of the purchase
        return total_price


product = Product("MacBook", 1450, 100)
print(product.name)
print(product.buy(2))
