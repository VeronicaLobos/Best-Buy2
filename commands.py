from products import LimitedProduct
"""
commands available through the user interface go here --------
note: pending handling KeyboardInterrupt error
"""


def print_all_products_store(my_store):
    """
    Command from the command dispatcher function:
    1. List all products in store

    Arg: my_store is a store object which contains a list of
        product objects. It has a method to return said
        product objects, and the product objects have a method
        that serializes their attributes into a string.

    Retrieves all product objects from the given store,
    formats each product's information into a string.
    Prints these strings in an ordered list.
    """
    products = my_store.get_all_products()

    if len(products) == 0:
        print("No products available at the moment")
    else:
        ordered_list = 1
        print("------")
        for product in products:
            print(f"{ordered_list}. {product.show()}")
            ordered_list += 1
        print("------")


def print_total_products(my_store):
    """
    Command from the command dispatcher function:
    2. Show total amount in store

    Checks if there are products in the store.
    Gets and iterates though every product object stored
    in the store object received as an argument, retrieves
    their quantity attribute and sums them.
    If the quantity attribute is a string, ignores it.
    Prints the total amount formated as a string.
    """
    if len(my_store.get_all_products()) == 0:
        print("Currently there aren't products available.")
        return

    total_amount = 0
    for product in my_store.get_all_products():
        quantity = product.get_quantity()
        if isinstance(quantity, (int, float)):
            total_amount += quantity

    print(f"Total of {total_amount} items in store")


def _check_amount(product_num, amount, product_list):
    """
    Utility command for the make_order command.

    Checks if a product is in range of the product
    object quantity attribute.
    Returns an integer, or raises an exception and
    interrupts the current loop that made the call.
    """
    try:
        product = product_list[product_num - 1]
        if isinstance(product.get_quantity(), str):
            return product
        elif 1 <= amount <= product.get_quantity():
            return product
    except AssertionError:
        print("Error while making order! Quantity larger than what exists")
        return


def _check_product_num(product_num, product_list):
    """
    Utility command for the make_order command.

    Checks if the input for product number is in range
    of ordered list of products from the store.
    Returns an integer, or raises an exception and
    interrupts the current loop that made the call.
    """
    try:
        assert 1 <= product_num <= len(product_list)
        return product_num
    except AssertionError:
        print("Error while making order! "
              "Please enter a valid product #")
        return


def make_order(my_store):
    """
    Command from the command dispatcher function:
    2. Show total amount in store

    Checks if there are products available in the store.

    Prints total price and updates product objects
    quantity attribute from store object.

    Lists all the products available in the store.
    Prompts the user for input and handles errors,
    empty input with an empty cart exits the command.
    Adds a tuple containing a product object and a
    quantity (int) to the cart (list).
    If the amount for the purchase is too large, returns
    to the menu.
    If the amount for LimitedProduct instance is larger
    than 1, returns to the menu.
    Sets cart_empty to False, keeps prompting the user
    for input until empty input.
    Calls a store method to receive total price, prints
    it formated as a string.

    If product quantity reaches 0, removes it from the store.
    """
    if len(my_store.get_all_products()) == 0:
        print("No products available!")
        return

    print_all_products_store(my_store) ########
    print("When you want to finish order, enter empty text.")

    product_list = my_store.get_all_products()
    cart = []
    cart_empty = True

    while True:
        try:
            product_num_str = input("Which product # do you want? ")
            amount_str = input("What amount do you want? ")
            input_empty = not product_num_str or not amount_str
            if cart_empty:
                if input_empty:
                    return
            elif input_empty:
                break  ## proceeds to order
            product_num = int(product_num_str)
            amount = int(amount_str)
        except ValueError:
            print("Error while making order")
            return

        if _check_product_num(product_num, product_list):
            product = _check_amount(product_num, amount, product_list)

            ## Order too large returns product = None
            if product is None:
                print("Error while making order! Quantity larger "
                      "than what exists")
                return

            ## Shipping limited to 1 unit per order
            if isinstance(product, LimitedProduct):
                if amount > 1:
                    print("Error while making order! Only 1 is allowed "
                      "from this product (Shipping)!")
                    return

            ## Add product to cart
            cart.append((product, amount))
            print("Product added to list!\n")
            cart_empty = False

    grand_total = my_store.order(cart)
    print(f"Order made! Total payment: ${grand_total}")
