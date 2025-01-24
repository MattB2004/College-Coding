class Animal:
    def __init__(self, name):
        self.name = name
    def speak():
        return f'{Animal.name} says booga ooga'
    def reply(self):
        return self.speak()


class Mammal(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says ooga booga!'


class Cat(Mammal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says Meow!'

class Dog(Mammal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says woof!'


class Primate(Mammal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says hello!'

class ComputerScientist(Primate):
    def __init__(self, name):
        self.name = name
