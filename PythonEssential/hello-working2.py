

def main():
	f = open("D:\Desarrollo\gitDev\gitPy\PythonLearning\PythonEssential\lines.txt") # modes r read  w write a append r+ read and write r+b binary r+t text t textmode
	for line in f:
		print(line.rstrip()) # this avoid dealing with endings

if __name__ == '__main__':main()


def main():
	infile = open("D:\Desarrollo\gitDev\gitPy\PythonLearning\PythonEssential\lines.txt", "rt")
	outfile = open("D:\Desarrollo\gitDev\gitPy\PythonLearning\PythonEssential\lines-copy.txt", "wt")

	for line in infile:
		print(line.rstrip(), file=outfile)
		print(".", end="", flush=True)
	outfile.write(line.rstrip())
	outfile.close()
	print("\ndone.")

if __name__ == '__main__':main()

#containers

x = (1,2,3,4,5)
y = list(reversed(x))
y = sum(x) # max min any
print(x)
print(y)
#zip
x = (1,2,3,4,5)
y = (6,7,8,9,10)

z = zip(x,y)
for a, b in z: print(f"{a} - {b}")

#order of values
x = ("cat", "dog", "rabbit")
for i, v in enumerate(x): print(f"{i}: {v}")


#modules

import sys
import os
import random
import datetime

def main():
	v = sys.version_info
	print("Python version {},{},{}".format(*v))
	y = sys.platform
	print(y)
	y = os.name
	print(y)
	y = os.getenv("PATH")
	print(y)
	y = os.getcwd()
	print(y)
	y = os.urandom(25).hex()
	print(y)

	x = random.randint(1, 1000)
	print(x)

	x = list(range(25))
	print(x)
	random.shuffle(x)
	print(x)

	now = datetime.datetime.now()
	print(now)
	print(now.year)



if __name__ == '__main__':main()