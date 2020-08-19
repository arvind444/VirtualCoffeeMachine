class CoffeeMachine:  # Define the class CoffeeMachine
    def __init__(self):  # Creating Instance Attributes for the Initial Value of coffee machine
        self.initial_water = 400
        self.initial_milk = 540
        self.initial_coffee_bean = 120
        self.initial_disposal_cup = 9
        self.initial_cash = 550
        self.choose = None
        self.fill_water = None
        self.fill_milk = None
        self.fill_coffee_bean = None
        self.fill_disposal_cup = None

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.choose = input()
        if self.choose == '1':  # To make espresso 250ml water, 16g coffee beans, $4 needed
            if self.initial_water < 250:
                print("Sorry, not enough water")
            elif self.initial_coffee_bean < 16:
                print("Sorry, not enough coffee beans")
            elif self.initial_disposal_cup < 1:
                print("Sorry, not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.initial_water -= 250
                self.initial_coffee_bean -= 16
                self.initial_disposal_cup -= 1
                self.initial_cash += 4
        elif self.choose == '2':  # To make latte 350ml water, 75ml of milk, 20g coffee beans, $7 needed
            if self.initial_water < 350:
                print("Sorry, not enough water")
            elif self.initial_milk < 75:
                print("Sorry, not enough milk")
            elif self.initial_coffee_bean < 16:
                print("Sorry, not enough coffee beans")
            elif self.initial_disposal_cup < 1:
                print("Sorry, not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.initial_water -= 350
                self.initial_milk -= 75
                self.initial_coffee_bean -= 20
                self.initial_disposal_cup -= 1
                self.initial_cash += 7
        elif self.choose == '3':  # To make cappuccino 200ml water, 100ml of milk, 12g coffee beans, $6 needed
            if self.initial_water < 200:
                print("Sorry, not enough water")
            elif self.initial_milk < 100:
                print("Sorry, not enough milk")
            elif self.initial_coffee_bean < 12:
                print("Sorry, not enough coffee beans")
            elif self.initial_disposal_cup < 1:
                print("Sorry, not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.initial_water -= 200
                self.initial_milk -= 100
                self.initial_coffee_bean -= 12
                self.initial_disposal_cup -= 1
                self.initial_cash += 6
        elif self.choose == 'back':
            pass
        else:
            print("Please enter the correct input")

    def fill(self):
        self.fill_water = int(input("Write how many ml of water do you want to add:"))
        self.fill_milk = int(input("Write how many ml of milk do you want to add:"))
        self.fill_coffee_bean = int(input("Write how many grams of coffee beans do you want to add:"))
        self.fill_disposal_cup = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.initial_water += self.fill_water
        self.initial_milk += self.fill_milk
        self.initial_coffee_bean += self.fill_coffee_bean
        self.initial_disposal_cup += self.fill_disposal_cup

    def take(self):
        print("I gave you ${}".format(self.initial_cash))
        self.initial_cash = 0  # After ttaking the money set the initial cash attribute to 0

    def remaining(self):
        print("The coffee machine has:")
        print("{} of water".format(self.initial_water))
        print("{} of milk".format(self.initial_milk))
        print("{} of coffee beans".format(self.initial_coffee_bean))
        print("{} of disposable cups".format(self.initial_disposal_cup))
        if self.initial_cash > 0:
            print("${} of money".format(self.initial_cash))
        else:
            print("{} of money".format(self.initial_cash))


def main_function():  # Define the main function for the Coffee Machine
    coffee_machine = CoffeeMachine()  # creating object for the class CoffeeMachine
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'buy':
            coffee_machine.buy()  # Calling the buy method in the class CoffeeMachine
        elif action == 'fill':
            coffee_machine.fill()  # Calling the fill method in the class CoffeeMachine
        elif action == 'take':
            coffee_machine.take()  # Calling the take method in the class CoffeeMachine
        elif action == 'remaining':
            coffee_machine.remaining()  # Calling the remaining method in the class CoffeeMachine
        elif action == 'exit':
            break
        else:
            print("Please Enter the correct input")


main_function()
