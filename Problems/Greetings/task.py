class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am {0}!".format(self.name))


my_person = Person(input())
my_person.greet()
