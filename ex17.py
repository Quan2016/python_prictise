from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copy file %s to file %s" %(from_file, to_file))

file_from = open(from_file)
data_from = file_from.read()
print("file %s  is %d bytes long" %(from_file, len(data_from)))
print("file %s is %r exists" %(to_file, exists(to_file)))
file_from.close()



file_to = open(to_file, 'w')
file_to.write(data_from)
file_to.close()

print("finished")
