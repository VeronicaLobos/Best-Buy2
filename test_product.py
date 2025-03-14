import pytest
from products import Product
import promotions


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
        Product(name="MacBook Air M2", price=-1450, quantity=100)


def test_product_becomes_inactive():
    """
    Tests that when a product reaches 0 quantity,
    it becomes inactive.
    """
    product = Product(name="MacBook Air M2", price=1450, quantity=100)

    ##  purchase as much as available
    purchase_amount = product.quantity
    product.buy(purchase_amount)

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

    ## Purchase everything available plus one unit
    purchase_amount = product.quantity + 1
    total_price = 0

    ## Should return a total price of 0
    assert product.buy(purchase_amount) == total_price
    ## Product quantity should remain unchanged
    assert product.quantity == purchase_amount - 1


#### Testing that promotion is assigned to product and applied

def test_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    second_half_price = (promotions.
                         SecondHalfPrice("Second Half price!"))
    product.set_promotion(second_half_price)

    assert product.promotion.name == "Second Half price!"
    assert product.buy(3) == 4350
    assert second_half_price.apply_promo(product, quantity=3) == 3625.0