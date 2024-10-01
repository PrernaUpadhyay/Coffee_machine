# ASCII art for the coffee cup
logo = r"""
                            *                               
   (                      (  `                 )            
 ( )\  (      (   (  (    )\))(      )      ( /(   (   (    
 )((_) )(    ))\  )\))(  ((_)()\  ( /(  (   )\()) ))\  )(   
((_)_ (()\\  /((_)((_)()\\ (_()((_) )(_)) )\\ (_))/ /((_)(()\\  
 | _ ) ((_)(_))  _(()((_)|  \\/  |((_)_ ((_)| |_ (_))   ((_) 
 | _ \\| '_|/ -_) \\ V  V /| |\\/| |/ _` |(_-<|  _|/ -_) | '_| 
 |___/|_|  \\___|  \\_/\\_/ |_|  |_|\\__,_|/__/ \\__|\\___| |_|   
"""


coffee_cup_art = r"""
         
                  ., '''''''''''''''''' ,.
               .'   .oooooo$$$$$ooooooo.   '.
              ::  ,$$$$$$$$$$$$$$$$$$$$$$,  ',
              |;  '$$$$$$$$$$$$$$$$$$$$$$'    ''''''''''.
              |;     ''''''$$$$$'''''''       ,:''''':, |
              |;   '|                   |'    ||      | |
              |;   '|                   |'    ||      | |
              |;   '|                   |'    ||      | |
              |;   '|                   |'    ||      | |
              |;   '|                   |'    ':.....:' |
              |;   '|                   |'     ,,,,,,,,,'
              |;   '|                   |'    ;
              |;.   |                   |   .'
               '||,,,                   ,,,;'
                  ''';;;;,,,,,,,,,,,;;;;'''
                         '''''''''''
"""

# ASCII art for the coffee machine
coffee_machine_art = r"""
                                             .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' met.
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'
"""

print(logo)
print(coffee_machine_art)
print(coffee_cup_art)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 120,  # ₹1.5 -> ₹120
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 205,  # ₹2.5 -> ₹205
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 245,  # ₹3.0 -> ₹245
    },
    "hot_cocoa_milk": {
        "ingredients": {
            "milk": 240,
            "cocoa_powder": 30,
            "sugar": 15,
        },
        "cost": 164,  # ₹2.0 -> ₹164
    }
}

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 100,
    "cocoa_powder": 50,
    "sugar": 30,
}

profit = 0
is_on = True


# Function to check if resources are sufficient
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


# Function to process rupees instead of dollars
def process_rupees():
    print("Please insert coins.")
    total = int(input("How many ₹100 coins?: ")) * 100
    total += int(input("How many ₹50 coins?: ")) * 50
    total += int(input("How many ₹20 coins?: ")) * 20
    total += int(input("How many ₹10 coins?: ")) * 10
    return total


# Function to check transaction success
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# Function to make the drink and deduct resources
def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/hot_cocoa_milk): ").lower()

    # If user presses enter without typing a valid drink name
    if choice == "":
        print("Please enter a valid choice.")
        continue

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Cocoa Powder: {resources['cocoa_powder']}g")
        print(f"Sugar: {resources['sugar']}g")
        print(f"Money: ₹{profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_rupees()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
    else:
        print(f"Sorry, '{choice}' is not a valid option. Please choose from the menu.")
