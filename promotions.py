from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, price, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity) -> float:
        return (quantity % 2 + quantity // 2 * 1.5) * price

    def __str__(self):
        return f"{self.name}"


class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity) -> float:
        return (quantity % 3 + quantity // 3 * 2) * price

    def __str__(self):
        return f"{self.name}"


class PercentDiscount(Promotion):
    def __init__(self, name, discount):
        super().__init__(name)
        self.discount = discount

    def apply_promotion(self, price, quantity) -> float:
        discount = price * self.discount / 100
        return (price - discount) * quantity

    def __str__(self):
        return f"{self.name}"


# product = products.Product("MacBook Air M2", price=1450, quantity=100)
# second_half_price = SecondHalfPrice("Second Half price!")

# promo = second_half_price.apply_promotion(product, 2)
# print(promo)
