class TheThing(object):
	#初始化方法， 初始变量， 初始值为0
	def __init__(self):
		self.number = 0
		
	def some_function(self):
		print("I got called.")
		
	def add_me_up(self, more):
		self.number += more
		return self.number
		
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))
print(a.number)
print(b.number)