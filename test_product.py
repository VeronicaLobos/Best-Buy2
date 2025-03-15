import pytest
from products import Product


def test_creating_product():
    """
    Tests that creating a normal product works.
    """
    product1 = Product(name="MacBook Air M2", price=1450, quantity=100)

    assert product1.name == "MacBook Air M2"
    assert product1.price == 1450
    assert product1.quantity == 100
    assert product1.is_active() == True


def test_creating_prod_invalid_details():
    """
    Tests that creating a product with invalid details
    (empty name, negative price) invokes an exception.
    """
    ##  Product name cannot be empty
    with pytest.raises(ValueError):
        Product(name="", price=1450, quantity=100)

    ##  Product price cannot be negative integer
    with pytest.raises(ValueError):
        Product(name="MacBook Air M2", price=-1450,
                quantity=100)


def test_product_becomes_inactive():
    """
    Tests that when a product reaches 0 quantity,
    it becomes inactive.
    """
    product = Product(name="MacBook Air M2", price=1450,
                      quantity=100)

    ##  purchase as much as available
    product.buy(product.quantity)
    assert product.is_active() is False


def test_buy_modifies_quantity():
    """
    Test that product purchase modifies the quantity
    and returns the right output.
    """
    product = Product(name="MacBook Air M2", price=1450, quantity=100)

    ## Purchase everything available except one unit
    purchase_amount = product.quantity - 1
    total_price = product.buy(purchase_amount)

    assert total_price == product.price * purchase_amount
    assert total_price == 1450 * 99
    assert product.quantity == 1


def test_buy_too_much():
    """
    Test that buying a larger quantity than exists
    invokes exception.
    """
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    error_msg = f"Not enough {product.name} units in store."

    with pytest.raises(ValueError, match = error_msg):
        ## Purchase everything available plus one unit
        product.buy(product.quantity + 1)
