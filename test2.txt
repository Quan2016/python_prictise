from sys import argv

script, filename = argv

#open the file
target = open(filename, 'w')

#truncate the file
target.truncate()

#something need to write
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

#write to file 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#closing the file
target.close()