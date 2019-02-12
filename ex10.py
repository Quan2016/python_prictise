tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat1 = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

x = "hello %d !" %250

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat1)
print(fat_cat2)
#print(fat_cat3)
print("he said:\"%s\"" %x)
print('he said:\"%r\"' %x)
