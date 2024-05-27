from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


money_ = MoneyMachine()
menu_ = Menu()
maker_ = CoffeeMaker()


Order = True

while Order:

    choice_ = input('What would you like? (espresso,latte,cappuccino): ').lower()

    if choice_ == "report":
        maker_.report()
    elif choice_ == "off":
        Order = False
    else:
        item_ = menu_.find_drink(choice_)
        make_ = maker_.is_resource_sufficient(item_)
        if make_:
            payment_ = money_.make_payment(item_.cost)

            if payment_:
                maker_.make_coffee(item_)
    clear()
