"""Menu of options"""
menu = {
   "espresso": {
      "ingredients": {
         "water": 50,
         "coffee": 18
      },
      "cost": 1.5
   },
   "latte": {
      "ingredients": {
         "water": 200,
         "coffee": 24,
         "milk": 150
      },
      "cost": 2.5
   },
   "cappuccino": {
      "ingredients": {
         "water": 250,
         "coffee": 24,
         "milk": 100
      },
      "cost": 3.0
   }
}

"""Default ingredient levels"""
ingredient_levels = {
    "water": 500,
    "coffee": 60,
    "milk": 500,
    
}

total_money = 0

def deduct_ingredients(drink):
    ingredient = drink["ingredients"]                                       #Calls ingredients dictionary for each item on menu
    ingredient_levels["water"] -= ingredient.get("water", 0)                #Subtracts amount of ingredients per drink from default ingredient levels. "0" is in place to handle missing ingredients
    ingredient_levels["coffee"] -= ingredient.get("coffee", 0)
    ingredient_levels["milk"] -= ingredient.get("milk", 0)
    
def check_ingredients_level(drink):                                         #Checks if ingredient levels are sufficient to make order. If not, the function returns False
    ingredients = drink["ingredients"]
    return (
        ingredient_levels["water"] >= ingredients.get("water", 0)
        and ingredient_levels["coffee"] >= ingredients.get("coffee", 0)
        and ingredient_levels["milk"] >= ingredients.get("milk", 0)
    )


def input_order(user_input):
    global total_money                                                      #Calls global variable
    drink = menu[user_input]
    drink_cost = drink["cost"]
    
    if not check_ingredients_level(drink):
        print("Insufficient ingredients. Please refill")
        return
    
    print(f"The price of a {user_input} is ${drink_cost}")
    print("Please insert coins.\n")
    
    inserted_coins = 0.00
    inserted_coins += int(input("How many quarters? ")) * .25
    inserted_coins += int(input("How many dimes? ")) * .10
    inserted_coins += int(input("How many nickels? ")) * .05
    inserted_coins += int(input("How many pennies? ")) * .01

    if inserted_coins < drink_cost:
        print("Insufficient funds. Coins refunded.")
        return
        
    elif inserted_coins > drink_cost:
        print(f"Here is ${round((inserted_coins - drink_cost), 3)} in change.")
        total_money += drink_cost
        
    else:
        total_money += drink_cost
        
    print("Enjoy your coffee!")
    deduct_ingredients(drink)

user_input = ""

while user_input != "exit":
    
    user_input = input("What would you like to order? Type 'exit' to exit: ").strip().lower()
    
    if user_input == "report":
        print(f"Water: {ingredient_levels["water"]}ml")
        print(f"Milk: {ingredient_levels["milk"]}ml")
        print(f"Coffee: {ingredient_levels["coffee"]}g")
        print(f"Money: ${total_money}")
        continue
        
    if user_input not in menu:
        print("That order is not available. Please try again.")
        continue
    
    input_order(user_input)