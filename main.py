import sys
from products import Product, NonStockedProduct, LimitedProduct
from store import Store
import promotions
import commands


# setup initial stock of inventory ---------------------------
def setup_inventory():
    """
    Creates and returns a store object:
    a list containing product objects.
    """
    ##  Setup initial stock of inventory
    product_list = [ Product(name="MacBook Air M2",
                             price=1450, quantity=100),
                 Product(name="Bose QuietComfort Earbuds",
                         price=250, quantity=500),
                 Product(name="Google Pixel 7",
                         price=500, quantity=250),
                 NonStockedProduct("Windows License",
                                   price=125),
                 LimitedProduct("Shipping", price=10,
                                quantity=250, maximum=1)]

    ##  Create promotion catalog
    second_half_price = (promotions.
                             SecondHalfPrice("Second Half price!"))
    third_one_free = (promotions.
                          ThirdOneFree("Third One Free!"))
    thirty_percent = (promotions.
                          PercentDiscount("30% off!", percent = 30))

    ##  Assign promotion to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    #### Testing that promotion is assigned to product and applied
    #print(product_list[0].promotion.name)
    #    >>> Second Half price!
    #print(product_list[0].buy(3))
    #    >>> 4350
    #print(second_half_price.apply_promo(product_list[0], quantity=3))
    #    >>> 3625.0

    return Store(product_list)


# commands for the user interface go here --------------------
def _command_dispatcher(user_input, my_store):
    """
    Utility command for the start function.

    Args: user_input, the key to access a value in the dict.
        my_store, given as a parameter for a function call.
    Pairs the menu options (key) with the functions
    available to the user in the CLI program (value).
    Returns a function call with a store object as
    parameter.
    """
    if user_input == 4:
        sys.exit()
    else:
        commands_dict = {
            1: commands.print_all_products_store, # tested
            2: commands.print_total_products,
            3: commands.make_order,
        }
        return commands_dict[user_input](my_store)


def _check_input():
    """
    Utility command for the start function.

    Asks user for input, a number between 1 and 4
    Else, will continue asking for a valid input.
    Handles errors if wrong value input or number
    out of range.
    Returns an integer between 1-4 (included)
    """
    while True:
        try:
            user_input = int(input("Please choose a number (1-4): "))
            assert 1 <= user_input <= 4
            return user_input
        except AssertionError:
            print("Number not valid")
            continue
        except ValueError:
            print("Error with your choice! Try again!")
            continue


def _print_menu():
    """
    Utility command for the start function.

    Prints a menu for the buyer with the
    command options available from the user
    interface.
    """
    print("\tStore Menu\n\t----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def start(store):
    """
    Starts the self-service terminal.
    Allows users to check products, inventory,
    make and order or exit the terminal.

    Gets the store object as a parameter,
    shows the user the menu.
    Checks user input.
    Calls a function chosen by the user.
    Prints a space after a command has
    successfully run and restarts.
    """
    while True:
        _print_menu()
        user_input = _check_input()
        _command_dispatcher(user_input, store)
        print("")


def main():
    """
    Opens a store, sets inventory.
    Starts a self-service terminal.
    """
    best_buy = setup_inventory()
    start(best_buy)


if __name__ == "__main__":
    main()