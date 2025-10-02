import pytest
from products import Product


def test_normal_functionality():
    """Test that creating a normal product works."""
    product = Product("MacBook", price=1450, quantity=100)
    assert product.name == "MacBook"
    assert product.price == 1450
    assert product.quantity == 100


def test_empty_name():
    """Test that creating a product with invalid details (empty name) invokes an exception."""
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_negative_price():
    """Test that creating a product with invalid details (negative price) invokes an exception."""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("MacBook", price=-1450, quantity=100)


def test_zero_quantity():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook", price=1450, quantity=100)
    product.buy(amount=100)
    assert product.is_active() == False


def test_modifies_quantity():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = Product("MacBook", price=1450, quantity=100)
    assert product.buy(2) == 2900


def test_larger_quantity():
    """Test that buying a larger quantity than exists invokes exception."""
    product = Product("MacBook", price=1450, quantity=100)
    with pytest.raises(
        ValueError, match="Error while making order! Quantity larger than what exists"
    ):
        product.buy(amount=102)


pytest.main()
