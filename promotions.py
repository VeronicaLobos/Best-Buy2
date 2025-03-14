from abc import ABC, abstractmethod


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
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promo(self, product, quantity):
        price_two_products = (quantity // 2) * (product.price * 1.5)
        price_if_remaining_item = (quantity % 2) * product.price

        return price_two_products + price_if_remaining_item


class ThirdOneFree(Promotion):
    """
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promo(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    """
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    """
    def __init__(self, name:str, percent:int):
        super().__init__(name)
        self.percent = percent

    def apply_promo(self, product, quantity):
        pass