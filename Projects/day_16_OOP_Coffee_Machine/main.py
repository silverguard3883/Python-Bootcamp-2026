from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on is True:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options})")
    
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) is True:
            if money_machine.make_payment(drink.cost) is True:
                coffee_maker.make_coffee(drink)







