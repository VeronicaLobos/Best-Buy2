
class Promotion:
    def __init__(self, name:str):
        self.name = name
        pass


class SecondHalfPrice(Promotion):
    """
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    """
    pass


class ThirdOneFree(Promotion):
    """
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    """
    pass


class PercentDiscount(Promotion):
    """
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    """
    pass