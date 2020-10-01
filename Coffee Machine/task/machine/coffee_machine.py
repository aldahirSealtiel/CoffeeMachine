class CoffeeMachine:

    def __init__(self):
        self.state = None
        self.available_water = 400
        self.available_milk = 540
        self.available_coffee = 120
        self.available_money = 550
        self.available_cups = 9

    def make_action(self, instruction):
        if instruction == "buy":
            print()
            self.buy()
        elif instruction == "fill":
            print()
            self.fill()
        elif instruction == "take":
            print()
            self.take()
        elif instruction == "remaining":
            print()
            self.print_state_machine()
        print()

    def print_state_machine(self):
        print("The coffee machine has:")
        print("{0} of water".format(self.available_water))
        print("{0} of milk".format(self.available_milk))
        print("{0} of coffee beans".format(self.available_coffee))
        print("{0} of disposable cups".format(self.available_cups))
        print("{0} of money".format(self.available_money))

    def buy(self):
        type_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if type_coffee == "back":
            return
        if int(type_coffee) == 1:
            if self.check_resources(250, 0, 16):
                self.available_water -= 250
                self.available_coffee -= 16
                self.available_money += 4
                self.available_cups -= 1
        elif int(type_coffee) == 2:
            if self.check_resources(350, 75, 20):
                self.available_water -= 350
                self.available_milk -= 75
                self.available_coffee -= 20
                self.available_money += 7
                self.available_cups -= 1
        elif int(type_coffee) == 3:
            if self.check_resources(200, 100, 12):
                self.available_water -= 200
                self.available_milk -= 100
                self.available_coffee -= 12
                self.available_money += 6
                self.available_cups -= 1

    def fill(self):
        water_to_add = int(input("Write how many ml of water do you want to add:"))
        milk_to_add = int(input("Write how many ml of milk do you want to add:"))
        coffee_to_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_to_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.available_water += water_to_add
        self.available_milk += milk_to_add
        self.available_coffee += coffee_to_add
        self.available_cups += cups_to_add

    def take(self):
        print("I gave you $", self.available_money)
        self.available_money = 0

    def check_resources(self, water, milk, coffee):

        if self.available_water - water < 0:
            print("Sorry, not enough water!")
            return False
        elif self.available_milk - milk < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.available_coffee - coffee < 0:
            print("Sorry, not enough coffee")
            return False
        elif self.available_cups - 1 < 0:
            return False
        print("I have enough resources, making you a coffee!")
        return True


action = input("Write action (buy, fill, take, remaining, exit):")
my_machine = CoffeeMachine()
while action != "exit":
    my_machine.make_action(action)
    action = input("Write action (buy, fill, take, remaining, exit):")
