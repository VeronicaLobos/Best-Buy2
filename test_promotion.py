import pytest
from products import Product


"""
Note: not required in the assignment,
just for practice and testing of my project
"""

def test_half_price_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    second_half_price = (promotions.
                         SecondHalfPrice("Second Half price!"))
    product.set_promotion(second_half_price)

    assert product.promotion.name == "Second Half price!"
    ##  Price without promotion, 1450 * 3
    assert product.buy(3) == 4350
    ##  Price with promotion , 1450 * 2.5
    assert second_half_price.apply_promo(product, quantity=3) == 3625.0


def test_third_one_free_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    third_one_free = (promotions.
                      ThirdOneFree("Third One Free!"))
    product.set_promotion(third_one_free)

    assert product.promotion.name == "Third One Free!"
    assert product.buy(3) == 4350
    assert third_one_free.apply_promo(product, quantity=0) == 0
    assert third_one_free.apply_promo(product, quantity=2) == 2900
    assert third_one_free.apply_promo(product, quantity=3) == 2900
    assert third_one_free.apply_promo(product, quantity=4) == 2900 + 1450
    assert third_one_free.apply_promo(product, quantity=5) == 2900 * 2


def test_percent_discount_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    thirty_percent = (promotions.
                          PercentDiscount("30% off!", percent = 30))
    product.set_promotion(thirty_percent)

    assert product.promotion.name == "30% off!"
    assert product.buy(7) == 10150
    assert thirty_percent.apply_promo(product, quantity=7) == 7105
