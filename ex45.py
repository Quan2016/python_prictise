#Animal 继承自 object
class Animal(object):
	pass
#Dog 继承自Animal
class Dog(Animal):
	
	def __init__(self, name):
		self.name = name
		
class Cat(Animal):
	
	def __init__(self, name):
		self.name = name
		
class Person(object):
	
	def __init__(self, name):
		self.name = name
		self.pert = None
		
class Employ(Person):
	
	def __init__(self, name, salary):
		super(Employ, self).__init__(name)
		self.salary = salary

class Fish(object):
	pass
	
class Salmon(Fish):
	pass
	
class Halibut(Fish):
	pass
	
rover = Dog("Lily")

sata = Cat("Dave")

mary = Person("Mary")
#pyton 不具备变量访问权限控制？
mary.pert = sata

frank = Employ("Saty", 120000)

frank.pert = rover

flipper = Fish()

