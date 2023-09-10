from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resource = CoffeeMaker()
money = MoneyMachine()
menu_list = Menu()
while True:
    user_choice = input(f" What would you like? {menu_list.get_items()}: ").lower()
    if user_choice == 'report':
        resource.report()
        money.report()
    else:
        drink_choice = menu_list.find_drink(user_choice)
        if resource.is_resource_sufficient(drink_choice):
            if money.make_payment(drink_choice.cost):
                resource.make_coffee(drink_choice)

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# should_continue = True
#
# def payment(cost):
#     """This will take in the cost of the coffee as input, and check if the customer has made enough payment,
#     return False if not, or return the change amount if they made enough payment."""
#     print("Please insert coins. ")
#     quarters = float(input("how many quarters?: "))
#     dimes = float(input("how many dimes?: "))
#     nickels = float(input("how many nickels?: "))
#     pennies = float(input("how many pennies?: "))
#
#     payment_amount = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
#
#     change = payment_amount - cost
#
#     if change < 0:
#         return 'False'
#     else:
#         return change
#
#
# def make_coffee(coffee):
#     """This takes in resources in form of a dictionary and menu ingredients -- another dictionary,
#     and outputs updated resource left if there is enough, or a canned message saying there isn't enough """
#
#     for item in MENU[coffee]['ingredients']:
#         if MENU[coffee]['ingredients'][item] > resources[item]:
#             return item
#     return 0
#
# def coffee_machine():
#
#     money = 0
#
#     while should_continue:
#
#         user_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
#
#         if user_choice == 'report':
#             print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${money}")
#         else:
#             resource = make_coffee(user_choice)
#             if resource != 0: #if there isn't enough resources to fulfill order
#                 print(f"Sorry there is not enough {resource}.")
#                 #should_continue = False
#             else:
#                 change = payment(MENU[user_choice]['cost'])
#                 if change == 'False':
#                     print("Sorry that's not enough money. Money refunded. ")
#                     #should_continue = False
#                 else:
#                     money += MENU[user_choice]['cost']
#                     for item in MENU[user_choice]['ingredients']:
#                         resources[item] -= MENU[user_choice]['ingredients'][item]
#                     print(f"Here is ${round(change, 2)} in change. ")
#                     print(f"Here is your {user_choice} ☕️. Enjoy! ")
#
#
# coffee_machine()
