#class deep
class Animal:

	def __init__(self, **kwargs):
		# this is how declare atributes only for the object
		if "type" in kwargs: self._type = kwargs["type"]
		if "name" in kwargs: self._name = kwargs["name"]
		if "sound" in kwargs: self._sound = kwargs["sound"]

	def type(self, t = None):
		if t: self._type = t
		try: return self._type
		except AttributeError: return None

	def name(self, n = None):
		if n: self._type = n
		try: return self._name
		except AttributeError: return None

	def sound(self, s = None):
		if s: self._sound = s
		try: return self._sound
		except AttributeError: return None

	def __str__(self):
		return f"The {self.type()} is named {self.name()} and says {self.sound()}"



class Duck(Animal): # inheritance
	def __init__(self, **kwargs):
		self._type = "duck"
		if "type" in kwargs: del kwargs["type"]
		super().__init__(**kwargs) # class the parent class

	def kill(self, s):
		print(f"{self.name()} will now kill all {s}!!")



def print_animal(o):
	if not isinstance(o, Animal):
		raise TypeError("print_animal(): requires an Animal")
	print(f"The {o.type()} is named {o.name()} and says {o.sound()}")

def main():
		#a0 = Animal("kitten", "fluffy", "rwar")
		a1 = Animal(type="kitten", name="fluffy", sound="rwar")
		#print_animal(a1)
		#a1.type("bear")
		a5 = Duck(name = "Donald", sound = "quack")
		a5.kill("humans")




if __name__ == '__main__': main()