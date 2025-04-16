from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    print("I can walk and run")
    input("What am I? ")

    def __init__(self,ans):
        self.ans = ans
        ans = Human

        if (self.ans == Human):
            print("You are correct")


class Snake(Animal):
    print("I can crawl")
    input("What am I?")

class Dog(Animal):
    print("I can bark")
    input("What am I?")

class Lion(Animal):
    print("I can roar")
    input("What am I?")


A = Human()
A.move()

B = Snake()
B.move()

A = Dog()
A.move()

B = Lion()
B.move()