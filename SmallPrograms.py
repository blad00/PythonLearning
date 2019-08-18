# x = int(raw_input("Please enter an integer: "))
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# los primos
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

    # %%%%%%%%%%%%
# Pares
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


def fib(n):  # write Fibonacci series up to n
    # """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


fib(20)

f = fib

f(500)
fib(0)

print(fib(0))


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


f100 = fib2(100)  # call it
f100  # write the result


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('refusenik user')
        print(complaint)


ask_ok('Do you really want to quit?')

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    # Dictionarios **, * tuple
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


write_multiple_items("/tmp/tt.txt", ":", "1", "2", "1000")

list(range(3, 6))  # normal call with separate arguments
args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
f(10)
f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


def my_function():
    """Do nothing, but document it.

	No, really, it doesn't do anything.
	"""
    pass


print(my_function.__doc__)

##chapter 5 LIST Ojooooo !!!!!!! always you need []
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()
fruits
# Lists as Stacks --> pila (“last-in, first-out”)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack

# Lists as Queues (“first-in, first-out”)
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
queue

# list comprehensions
squares = [x ** 2 for x in range(10)]
# instead of
squares2 = []
for x in range(10):
    squares2.append(x ** 2)

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# instead of
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# apply a function to all the elements
[abs(x) for x in vec]
# call a method on each element, strp in this case
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# the tuple must be parenthesized, otherwise an error is raised
#[x, x**2 for x in range(6)]

#5.1.4. Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
#The following list comprehension will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)]
#less comprehen
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

#no comprenhen
transposed = []
for i in range(4):
# the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

#zip does that
list(zip(*matrix))

#5.2. The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]
a
del a

#5.3. Tuples and Sequences
t = 12345, 54321, 'hello!'
t[0]
t
u = t, (1, 2, 3, 4, 5)
u
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 10

#empty or one size tuple
empty = ()
singleton = 'hello',
len(empty)
len(singleton)
singleton
x, y, z = t
#5.4. Sets
