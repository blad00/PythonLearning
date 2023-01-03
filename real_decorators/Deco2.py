# Timing Functions

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(999)

# Debugging Code

import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Benjamin")
make_greeting("Richard", age=112)

import math

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

approximate_e(10)

# Slowing Down Code

import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)

# Registering Plugins

import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

PLUGINS
randomly_greet("Alice")

globals()

# Is the User Logged In?

# from flask import Flask, g, request, redirect, url_for
# import functools
# app = Flask(__name__)
#
# def login_required(func):
#     """Make sure user is logged in before proceeding"""
#     @functools.wraps(func)
#     def wrapper_login_required(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for("login", next=request.url))
#         return func(*args, **kwargs)
#     return wrapper_login_required
#
# @app.route("/secret")
# @login_required
# def secret():

# Decorating Classes

from real_decorators.decorators import debug, timer


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])

tw = TimeWaster(1000)
tw.waste_time(999)

from real_decorators.decorators import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

tw = TimeWaster(1000)
tw.waste_time(999)

# Nesting Decorators

from real_decorators.decorators import debug, do_twice

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")

greet("Eva")

# Decorators With Arguments
from real_decorators.decorators import repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("World")


@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

say_whee()
greet("Penny")

# Stateful Decorators
from real_decorators.decorators import count_calls

@count_calls
def say_whee():
    print("Whee!")

say_whee()
say_whee()
say_whee.num_calls

# Classes as Decorators

class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

counter = Counter()
counter()
counter()
counter.count


from real_decorators.decorators import CountCalls
@CountCalls
def say_whee():
    print("Whee!")

say_whee()
say_whee()
say_whee()
say_whee()
say_whee.num_calls

# More Real World Examples

# Slowing Down Code, Revisited
from real_decorators.decorators import slow_down

@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(5)

# singleton

from real_decorators.decorators import singleton

@singleton
class TheOne:
    pass

first_one = TheOne()
another_one = TheOne()

id(first_one)
id(another_one)
first_one is another_one

# Caching Return Values

from real_decorators.decorators import count_calls

@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(15)

fibonacci.num_calls

from real_decorators.decorators import count_calls, cache


# faster
@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(15)
fibonacci(100)
fibonacci(8)

import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(15)
fibonacci(100)
fibonacci(8)
fibonacci(5)

fibonacci.cache_info()

# units

import math
from real_decorators.decorators import set_unit

@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height

volume(3, 5)
volume.unit

# Validating JSON

