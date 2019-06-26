#x = int(raw_input("Please enter an integer: "))
x=1
if x < 0:
    x = 0
    print ('Negative changed to zero')
elif x == 0:
    print ('Zero')
elif x == 1:
    print ('Single')
else:
    print ('More')

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

#los primos
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'
#Pares
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

def fib(n):    # write Fibonacci series up to n
    #"""Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(2000)

f = fib

f(500)
fib(0)

print fib(0)


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

ask_ok('Do you really want to quit?')

i = 5

def f(arg=i):
    print arg

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


#Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            "sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

write_multiple_items("C:/Users/Blado/Downloads/tt.txt",":","1","2","1000")

range(3, 6)             # normal call with separate arguments
args = [3, 6]
range(*args)            # call with arguments unpacked from a list

def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print my_function.__doc__

##LIST

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')

a.insert(2, -1)
a.append(333)
a.index(333)
a.remove(333)
a.reverse()
a.sort()
a.pop()

print(a)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival

def f(x): return x % 3 == 0 or x % 5 == 0

filter(f, range(2, 25))

def cube(x): return x*x*x

map(cube, range(1, 11))

seq = range(8)
def add(x, y): return x+y
map(add, seq, seq)

def add(x,y): return x+y
reduce(add, range(1, 11))

def sum(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 0)

    sum(range(1, 11))

    sum([])
