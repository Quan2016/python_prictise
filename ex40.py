cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities["NY"] = 'New York'
cities["OR"] = 'Portland'

def find_city(themap, state):
	#循环key，查找key的value
	if state in themap:
		return themap[state]
	else:
		return "Not fount."
#将_find 作为key find_city方法作为value		
cities['_find'] = find_city

while True:
	print("State? (Enter to quit)"),
	state = input("> ")
	#如果不为空
	if not state: break
	
	city_found = cities['_find'](cities, state)
	print(city_found)