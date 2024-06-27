from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

turn_off = False

while not turn_off:
    choice = input('What would you like? (' + menu.get_items() +'): ').lower()
    
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        turn_off = True
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        
                


     