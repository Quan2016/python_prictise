from sys import argv

script, input_file = argv
#打印全部
def print_all(f):
	print(f.read())

#将指针定位到第一行
def rewind(f):
	f.seek(0)#0开始位置，1当前位置，2结束位置
#打印特定行
def print_a_line(line_count, f):
	print(line_count, f.readline())
#打开文件
current_file = open(input_file)

#print the whole file
print_all(current_file)
#rewind
rewind(current_file)
#print tree line_count
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)