print("You enter a dark room with two doors. Do you go through door #1 or door #2")

door = input("> ")

if door == '1':
	print("Welcome to chicken!")
	print("1.take the cake.")
	print("2.Scream at the bear")
	
	bear = input("> ")
	
	if(bear == "1"):
		print("good job! bear eate your cake!")
	elif(bear == "2"):
		print("good job! bear eats your legs off.")
	else:
		print("well, you do noting")
