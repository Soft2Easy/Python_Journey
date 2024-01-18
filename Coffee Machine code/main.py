MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

REPORT = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def calc(quarters, dime, nickles, pennies):
    currency_ = [0.25, 0.10, 0.05, 0.01]

    currency_[0] *= quarters
    currency_[1] *= dime
    currency_[2] *= nickles
    currency_[3] *= pennies

    return sum(currency_)


def balance(price, amount):
    return amount - price


def report_update(report, menu, choice):
    if choice != "espresso":
        report["water"] -= menu[choice]["ingredients"]["water"]
        report["milk"] -= menu[choice]["ingredients"]["milk"]
        report["coffee"] -= menu[choice]["ingredients"]["coffee"]
        report["money"] += menu[choice]["cost"]
    else:

        report["water"] -= menu[choice]["ingredients"]["water"]
        report["coffee"] -= menu[choice]["ingredients"]["coffee"]
        report["money"] += menu[choice]["cost"]

    if report["water"] < 0:
        return "water"
    elif report["milk"] < 0:
        return "milk"
    elif report["coffee"] < 0:
        return "coffee"
    else:
        return report


def report_display(report):
    print(f'Water: {report["water"]}')
    print(f'Milk: {report["milk"]}')
    print(f'Coffee: {report["coffee"]}')


order_ = True

while order_:

    choice_ = input('What would you like? (Espresso/Latte/Cappuccino): ').lower()

    if choice_ == "report":
        report_display(REPORT)
    elif choice_ == "off":
        order_ = False
    else:

        print('Please insert coin')
        quarters_ = int(input('how many quarters?: '))
        dime_ = int(input('how many dime?: '))
        nickles_ = int(input('how many nickles?: '))
        pennies_ = int(input('how many pennies?: '))

        amount_ = calc(quarters_, dime_, nickles_, pennies_)

        item_cost_ = MENU[choice_]["cost"]

        if amount_ > item_cost_:
            balance_ = balance(item_cost_, amount_)
            report_ = report_update(REPORT, MENU, choice_)

            if report_ == "water" or report_ == "coffee" or report_ == "milk":
                print(f'Sorry there is not enough {report_}')
            else:
                print(f'here is ${balance_} in change.')
                print(f'here is your {choice_}. Enjoy')
                REPORT = report_
        else:
            print('Sorry that is not enough money. Money refunded.')
