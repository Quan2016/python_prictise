the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'banana', 'peers']

for number in the_count:
	print("This is count %d" %number)

for fruit in fruits:
	print("A fruit of type: %s" %fruit)

element = []
for i in range(0, -8, -1):
	print("Adding %d in the list." %i)
	#append element to list 
	element.append(i)

for i in element:
	print("Element was : %d" %i)