from products import Product
import promotions


"""
A module containing test for the Promotion class.
Mainly checks if promotions are applied to instances
of the Product class during the buy product process
and from the promotion itself.

Note: not required in the assignment,
just for practice and testing of my project :)
"""

def test_half_price_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    ##  Price without promotion, 1450 * 3
    assert product.buy(3) == 4350

    ## Apply promotion
    second_half_price = (promotions.
                         SecondHalfPrice("Second Half price!"))
    product.set_promotion(second_half_price)

    ##  Price with promotion, 1450 * 2.5
    assert product.promotion.name == "Second Half price!"
    assert product.buy(3) == 3625
    assert second_half_price.apply_promo(product, quantity=3) == 3625


def test_third_one_free_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    ## Price without promotion
    assert product.buy(3) == 4350

    ## Apply promotion
    third_one_free = (promotions.
                      ThirdOneFree("Third One Free!"))
    product.set_promotion(third_one_free)

    ##  Price with promotion
    assert product.promotion.name == "Third One Free!"
    assert product.buy(3) == 2900
    assert third_one_free.apply_promo(product, quantity=0) == 0
    assert third_one_free.apply_promo(product, quantity=2) == 2900
    assert third_one_free.apply_promo(product, quantity=3) == 2900
    assert third_one_free.apply_promo(product, quantity=4) == 2900 + 1450
    assert third_one_free.apply_promo(product, quantity=5) == 2900 * 2


def test_percent_discount_promo_applied():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    ## Price without promotion
    assert product.buy(7) == 10150

    ## Apply promotion
    thirty_percent = (promotions.
                          PercentDiscount("30% off!", percent = 30))
    product.set_promotion(thirty_percent)

    ##  Price with promotion
    assert product.promotion.name == "30% off!"
    assert product.buy(7) == 7105
    assert thirty_percent.apply_promo(product, quantity=7) == 7105
