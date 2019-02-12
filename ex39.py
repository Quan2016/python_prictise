ten_things = "1 2 3 4 5 6"

print("Wait! there are not enaugh ten things let's fixed it")

stuff = ten_things.split(" ")
#Array was split by ',' but not ' '
more_stuff = ["China", "Ammeriaca", "England", "Turkey", "Japan"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("we add %s into list" %next_one)
	stuff.append(next_one)
	print("There' %d items now." %len(stuff))

print("There we go, ", stuff)
#like java, item can be param to print
print("{},stuff[1]:", stuff[1])
print("stuff[-1]", stuff[-1])
print("stuff.pop():", stuff.pop())
#function join([])
print("\" \".join(stuff), ", " ".join(stuff))
print("'#'.join(stuff[3:5])", '#'.join(stuff[3:5]))