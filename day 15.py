# coffee machine project
# features
# 3 hot flavors
# coins operate
# automatic cup dispenser
# counting cup selling

# requirements: 50 ml water, 18g coffee
# 200 ml water, 24g coffee, 150 ml milk
# 250 ml water, 24g coffee, 100 ml milk
# price: 1.5; 2.5; 3
# machine resources 300 ml water, 200 ml milk, 100g coffee
# coins: penny - 1 cent, nickel - 5 cents, dime - 10 cents, quarter - 25 ml
# print report - check resources
# type of coffee
# insert money
# give change
# check transaction
# make the coffee


def money():
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))
    money_given = penny*0.01 + nickel*0.05 + dime*0.1+quarter*0.25
    change = money_given - price
    if money_given < price:
        print("Sorry, that's not enough for the coffee. Here's your money back.")
    else:
        print(f"Change: {change}$.\nEnjoy your coffee :)")


def resource_check():
    for j in range(0, len(resources)):
        if resources[j] - resource[j] < 0:
            print(f"Not enough {resources_name[j]}. Please refill")
            return False
        else:
            return True


def use_resources():
    for k in range(0, len(resources)):
        resources[k] -= resource[k]
    money()


def make_coffee(amount):
    resource_check()
    if resource_check() is True:
        use_resources()
        return amount
    else:
        pass
        return 0


flavours = ['espresso', 'latte', 'cappuccino']
resources_name = ['Water', 'Coffee', 'Milk']
resources = [3000, 1000, 2000]
money_in_machine = 0
status = True
while status is True:
    choice = input(f"What would you like? ({flavours[0]}/{flavours[1]}/{flavours[2]})")
    if choice == 'off':
        print("turning machine off")
        status = False
    elif choice == 'espresso':
        resource = [50, 18, 0]
        price = 1.5
        money_in_machine += make_coffee(price)
    elif choice == 'latte':
        resource = [200, 24, 150]
        price = 2.5
        money_in_machine += make_coffee(price)
    elif choice == 'cappuccino':
        resource = [250, 24, 100]
        price = 3
        money_in_machine += make_coffee(price)
    elif choice == 'report':
        print(f"Water: {resources[0]} ml\nCoffee: {resources[1]} ml\nMilk {resources[2]} g\nMoney: {money_in_machine}$")
    elif choice == 'refill':
        resources = [300, 100, 200]
        print(f"{resources[0]}, {resources[1]}, {resources[2]} refilled")
