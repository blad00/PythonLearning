# Functions

def add_one(number):
    return number + 1


add_one(2)


# First-Class Objects

def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


greet_bob(say_hello)

greet_bob(be_awesome)


# Inner Functions

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()


# Returning Functions From Functions

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

first
second

first()
second()


# Simple Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

say_whee()

say_whee

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

say_whee()


# Syntactic Sugar!

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()

# Reusing Decorators

from real_decorators.decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()


@do_twice
def greet(name):
    print(f"Hello {name}")


say_whee()
greet("World")

# Returning Values From Decorated Functions
from real_decorators.decorators import do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)

print
print.__name__
help(print)

say_whee
say_whee.__name__
help(say_whee)

say_whee
say_whee.__name__
help(say_whee)
