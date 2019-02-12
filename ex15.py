from sys import argv

script, filename = argv#解包

txt = open(filename)#打开文件，并返回文件变量

print("Here's your file %r:" %filename)
print(txt.read())#文件读取并打印

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())