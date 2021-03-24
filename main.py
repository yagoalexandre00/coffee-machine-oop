# Coffee Machine with OOP
# Author >>> Yago Goltara

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
from os import system
from time import sleep

def enter():
    sleep(1)
    input('Press ENTER to continue...')
    system('cls')


drinktable = PrettyTable()
menutable = PrettyTable()

menutable.add_column("ID",["1","2","3",])
menutable.add_column("COMMAND", ["Make Coffee", "Report", "Exit"], align= 'l') 

drinktable.add_column("      ",["1", "2", "3"])
drinktable.add_column("DRINKS", ["Cappuccino", "Espresso", "Latte"])

turn_on = True

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while turn_on == True:
    print(menutable)
    option = int(input("Insert the command: "))

    if option == 1:
        system('cls') 
        print(drinktable)
        user_choice = input("Type the drink's name you want: ").lower()
        drink = menu.find_drink(user_choice)
        is_resource_suf = coffee_machine.is_resource_sufficient(drink)
        if is_resource_suf == True:
            is_money_suf = money_machine.make_payment(drink.cost)
            if is_money_suf == True:
                coffee_machine.make_coffee(drink)
    elif option == 2:
        coffee_machine.report()
        money_machine.report()
    elif option == 3:
        turn_on = False
    else:
        print("Insert a valid command...")
    enter()