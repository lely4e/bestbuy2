import sys
from products import Product, NonStockedProduct, LimitedProduct
import store
import promotions


def display_menu():
    """Display the menu"""
    print(
        """
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """
    )


def show_product_items(store_object):
    """Show all products in the list"""
    product_items = store_object.get_all_products()
    for i, product in enumerate(product_items, start=1):
        print(f"{i}. ", end="")
        print(product)


def list_all_products(store_object):
    """List all products"""
    print("------")
    show_product_items(store_object)
    print("------")


def show_total_amount(store_object):
    """Display total amount"""
    print("------")
    print(f"Total of {store_object.get_total_quantity()} items in store")
    print("------")


def make_order(store_object):
    """Make an order"""
    print("------")
    show_product_items(store_object)
    print("------")
    print("When you want to finish order, enter empty text.")

    product_items = store_object.get_all_products()
    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ")
        amount = input("How many items do you want? ")

        if product_input == "" or amount == "":
            break

        product = None
        try:
            product_input = int(product_input)
            amount = int(amount)
            if product_input < 0:
                raise IndexError
            product = product_items[product_input - 1]
        except ValueError:
            print("Please enter a number.")
            continue
        except IndexError:
            print("No product with that number.")
            continue

        shopping_list.append((product, amount))
        print("Product added to list!")

    try:
        price = store.Store.order(shopping_list)
        print("\n*******")
        print(f"Order made! Total payment is: ${price}")
    except ValueError as value_error:
        print(value_error)


def options(store_object):
    """Display options"""
    choices = {1: list_all_products, 2: show_total_amount, 3: make_order}
    user_choice = input("Please choose a number: ")

    try:
        user_choice = int(user_choice)
    except ValueError:
        user_choice = None

    if user_choice == 4:
        sys.exit()

    if user_choice in choices:
        action = choices.get(user_choice)
        if action:
            action(store_object)
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")


def main():
    """Main Application"""
    # setup initial stock of inventory
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", discount=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = store.Store(product_list)

    while True:
        display_menu()
        options(best_buy)


if __name__ == "__main__":
    main()
