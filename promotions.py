from abc import ABC, abstractmethod

"""
A module to create Promotion instances and
apply them to Product instances.
If a Promotion has been applied, the total_price
will be modified when a product is bought.
"""

class Promotion(ABC):
    """
    A Promotion abstract class.
    Instantiated promotions get a name assigned.
    """
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def apply_promo(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    """
    Applies a "buy one, get the second at half-price" promotion.
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promo(self, product, quantity):
        """
        For every pair of units the final price will be 1.5 times
        the price of the item.
        When the quantity is odd, the price of a single unit will be
        added to the price.
        Returns the price after applying the promotion.
        """
        price_pairs = quantity // 2 * product.price * 1.5

        if quantity == 1:
            return product.price
        elif quantity % 2 == 0: # for odd quantities
            return price_pairs
        else:
            return price_pairs + product.price


class ThirdOneFree(Promotion):
    """
    Applies a "buy three, pay too" promotion.
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promo(self, product, quantity):
        """
        For every set of 3 units the final price will be 2 times
        the price of the item.
        When there are units not in sets of 3, it will add to the price
        the remainder units times the price of a single unit.
        Returns the price after applying the promotion.
        """
        price_set_of_three = (quantity // 3) * (product.price * 2)

        if 0 <= quantity <= 2:
            return product.price * quantity
        elif quantity % 3 == 0: # for quantities multiple of 3
            return price_set_of_three
        else:
            units_without_promo = (quantity % 3) * product.price
            return price_set_of_three + units_without_promo


class PercentDiscount(Promotion):
    """
    Applies a "total price minus %30 promotion" promotion.
    """
    def __init__(self, name:str, percent:int):
        super().__init__(name)
        self.percent = percent

    def apply_promo(self, product, quantity):
        """
        Calculates the percentage that will be charged
        from the full price of the items.
        Returns the price after applying the promotion.
        """
        percentage_to_pay = 100 - self.percent
        percentage_to_pay_as_decimal = percentage_to_pay / 100

        full_price = product.price * quantity

        return int(full_price * percentage_to_pay_as_decimal)
