class Animal:

    legs = 4

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def intro(self):
        print("Hi! I am a pet")


class Cat(Animal):

    def meow(self):
        print("Meow......")


class Dog(Animal):

    def bark(self):
        print("Woof......")


petDog = Dog("Beethoven", "Brown")
petDog.intro()
print("My name is {}. My colour is {}. I have {} legs.".format(petDog.name, petDog.colour, petDog.legs))
petDog.bark()

