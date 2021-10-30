# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        # print("dog initialized!")

    def bark(self):
        print("Woof!")

    def rollover(self):
        print("<<dog.name>> rolls over")

    def sit(self):
        print("<<dog.name>> sits")

# instantiation call that creates a Dog object:
my_dog = Dog("Rex", "SuperDog")
# my_dog.bark()
