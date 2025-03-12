
class Store:
    """
    Holds a single value: a list holding instances of the
    Products class.
    Allows the user to make a purchase of multiple products
    at once: product.buy()
    """
    stored = []

    def __init__(self, products: list):
        for product in products:
            Store.stored.append(product)


    def add_product(self, product):
        """
        Adds a product instance to 'stored'.
        """
        Store.stored.append(product)


    def remove_product(self, product):
        """
        Removes a product from 'stored'.
        """
        Store.stored.remove(product)


    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.
        """
        return len(Store.stored)


    def get_all_products(self):
        """
        Returns all products in the store that are active.
        If there aren't any products, returns an empty list.
        """
        active_products = []
        for product in Store.stored:
            if product.is_active():
                active_products.append(product)

        if len(active_products) >= 1:
            return active_products
        else:
            return []


    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        If the user inserts by mistake a string instead of a
        number for the quantity, the function will not include
        the product in the order.
        Buys the products and returns the total price of the order.
        """
        grand_total = 0

        for product in shopping_list:
            scan = product[0].buy(product[1])
            if not isinstance(scan, int):
                scan = 0
            grand_total += scan

        return grand_total
