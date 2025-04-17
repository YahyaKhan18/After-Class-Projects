from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    print("I can walk and run")
    print("1.Cat")
    print("2.Human")
    answer = input("What am I? ")

    if answer == "1":
        print("You are wrong!")
    else:
        print("You are right!")


class Snake(Animal):
    print("I can crawl")
    print("1.Snake")
    print("2.Capybara")
    answer = input("What am I? ")

    if answer == "2":
        print("You are wrong!")
    else:
        print("You are right!")


class Dog(Animal):
    print("I can bark")
    print("1.Elephant")
    print("2.Dog")
    answer = input("What am I? ")

    if answer == "1":
        print("You are wrong!")
    else:
        print("You are right!")


class Lion(Animal):
    print("I can roar")
    print("1.Lion")
    print("2.Monkey")
    answer = input("What am I? ")

    if answer == "2":
        print("You are wrong!")
    else:
        print("You are right!")



A = Human()
A.move()

B = Snake()
B.move()

A = Dog()
A.move()

B = Lion()
B.move()