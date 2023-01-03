

print("hello world")

import platform

print("this is python version {}".format(platform.python_version()))

def main():
	message()

def message():
	print("this is python version method {}".format(platform.python_version()))

if __name__ == '__main__': main()

x = 42
#print("hello {}".format(x))
print(f"hello {x}")

x = 42
y = 73

if x < y:
	print(f" {x < y}: x is {x} and y is {y}")

words = ["one", "two", "three", "four", "five"]

#Loops

##While
n = 0

while(n < 5):
	print(words[n])
	n += 1

#fibonachi

a, b = 0, 1

while b < 1000:
	print(b, end = " ", flush = True)
	#print(b)
	a, b = b, a + b

print()

##For

words = ["one", "two", "three", "four", "five"]

for i in words:
	print(i)


#Functions

#def function(n):
def function(n = 1): #With default value
	print(n)
	return n * 8

function()

x = function(11)
print(x)

def isprime(n):
	if n <= 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			return False
	else:
		return True

n = 6

if isprime(n):
	print(f"{n} is prime")
else:
	print(f"{n} not prime")

def list_primes():
	for n in range(100):
		if isprime(n):
			print(n, end=" ", flush=True)
	print()

list_primes()

#Classes

class Duck:

	sound = "Quaaaaack!"
	walking = "Walks like a duck"

	def quack(self):
		print(self.sound)

	def walk(self):
		print(self.walking)

def main():
	donald = Duck();
	donald.quack()
	donald.walk()

if __name__ == '__main__': main()


x = "seven".upper()
print(f"x is {x}")
print(type(x))

x = "seven {1} {0}".format(8,9)
print(f"x is {x}")
print(type(x))


a = 8
b = 9
x = f'seven {a:<09} {b:>09}'
print(f"x is {x}")
print(type(x))

x = 7 / 3
print(f"x is {x}")
print(type(x))

#careful with decimals or money you might need
# from decimal import *

#boolean
x = None
print(f"x is {x}")
print(type(x))

if x:
	print("True")
else:
	print("False")

#False = 0, "", None

##Sequence type
#list
x = [1,2,3,4,5]

x[2] = 42

for i in x:
	print(f"i is {i}")

#tuple
x = (1,2,3,4,5)
x = range(5,50, 5) # start, end, increment
for i in x:
	print(f"i is {i}")

#Dict
x = {"one":1, "two":2, "three":3, "four":4, "five":5}

for k,v in x.items():
	print(f"k: {k}, v: {v}")

#Type
#tuple
x = (1,2,"sss",4,5)
y = (1,2,"sss",4,5)
print(f"x is {x}")
print(type(x))
print(id(x))
print(id(y))

print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]:

	if x is y:
		print("yep")
	else:
		print("nope")

if isinstance(x, tuple):
	print("yep")
else:
	print("nope")


#Conditional
hungry = True
x = "feed now" if hungry else "do not feed the bear"
print(x)


#while

secret = "too"
pw = ""

while pw != secret:
	pw = input("input key workd? ")

#for

#loop control

def main():
	kitten("www", "eeeee", "pppp")

def kitten(*args):
	if len(args):
		for s in args:
			print(s)
	else: print("Mew")

if __name__ == '__main__': main()

#decorations

def f1(f):
	def f2():
		print("this is before")
		f()
		print("this is after")
	return f2

@f1
def f3():
	print("this is f3")

f3()

#useful decoration

import time

def elapse_time(f):
	def wrapper():
		t1 = time.time()
		f()
		t2 = time.time()
		print(f'Elapsed time: {(t2 - t1) * 1000} ms')
	return wrapper

@elapse_time
def big_sum():
	num_list = []
	for num in (range(0, 10000)):
		num_list.append(num)
	print(f"Big sum: {sum(num_list)}")

def main():
	big_sum()

if __name__ == '__main__': main()

#print set

a = set("La  casa me asusta")
b = set("a mi me gusta mucho")

def print_set(o):
	print('{', end='')
	for x in o: print(x, end = '')
	print('}')

c = a&b
print_set(c)


#list comprenhension

def print_list(o):
	for x in o: print(x, end= ' ')
	print()

seq = range(11)
seq2 = [x * 2 for x in seq] # times 2
seq3 = [x for x in seq if x % 3 != 0] # not divisble by 3
seq4 = [(x,x**2) for x in seq]
print_list(seq)
print_list(seq2)
print_list(seq3)
print_list(seq4)


#exceptions

import sys

def main():
	try:
		x = 5/0
	except ValueError:
		print("I have value error")
	# except ZeroDivisionError:
	# 	print("dont divide by 0")
	except:
		print(f"Unknonw error: {sys.exc_info()[1]}" )
	else:
		print("goo job")
		print(x)

if __name__ == '__main__': main()


#own exceptions
numargs = 5

try:
	if numargs > 2:
		raise TypeError(f"excpected less than {numargs}")
except TypeError as e:
	print((f"error mio: {e}"))


#String

print("Hello World".upper())
print("Hello World".swapcase())
print("Hello World. {}".format(45-8))
print("""
Hello 
World. {}
"""	  .format(45 - 8))

# separator
x = 42 * 789 * 85
#American
print("hello {:,}".format(x))
#Euro
print("hello {:,}".format(x).replace(",","."))
#decimal places
print("hello {:.3f}".format(x))
# binary
print("hello {:b}".format(x))
# decimal places
print(f"hello {x:.3f}")
# binary
print(f"hello {x:b}")

#Splitting joining
s = "Hola amiguitos como estan"
print(s.split()) #list separated by spaces
print(s.split("i"))  # list separated by i
l = s.split()
s2 = ":".join(l)
print(s2)

