poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------------")
print(poem)
print("--------------------")

five = 10 - 2 + 3 - 6
print("This should be five :%s" %five)
#function secret_formula
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans /1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With startirng point of :%d" %start_point)
#surport multy parameters
print("We'd have %d beans, %d jars,and %d crates." %secret_formula(start_point))
