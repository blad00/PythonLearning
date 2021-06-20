#class deep
class Animal:

	x = [1,2,3] # this is global for any object of this class

	#a0
	# def __init__(self, type, name, sound):
	# 	self._type = type
	# 	self._name = name
	# 	self._sound = sound

	#or a1
	def __init__(self, **kwargs):
		# this is how declare atributes only for the object
		self._type = kwargs["type"] if "type" in kwargs else "kitten" # with default variable
		self._name = kwargs["name"]
		self._sound = kwargs["sound"]

	def type(self, t = None):
		if t: self._type = t
		return self._type

	def name(self):
		return self._name

	def sound(self):
		return self._sound

	def __str__(self):
		return f"The {self.type()} is named {self.name()} and says {self.sound()}"

def print_animal(o):
	if not isinstance(o, Animal):
		raise TypeError("print_animal(): requires an Animal")
	print(f"The {o.type()} is named {o.name()} and says {o.sound()}")

def main():
		#a0 = Animal("kitten", "fluffy", "rwar")
		a1 = Animal(type="kitten", name="fluffy", sound="rwar")
		#print_animal(a1)
		a1.type("bear")
		print(a1)




if __name__ == '__main__': main()