# #file creation

# file=open("demo.txt",'w')
# file.close()


# #read file
#
# file=open("demo.txt",'r')
# content=file.read()
# print(content)
# file.close()

# #to read a single line
#
# file=open("demo.txt",'r')
# content=file.readline()
# print(content)
# file.close()

# #to read a specific number of bytes
#
# file=open("demo.txt",'r')
# content=file.read(10)
# print(content)
# file.close()

# #to write into a file/to replace contents of a file
#
# file=open("demo.txt",'w')
# file.write("am python django")
# file.close()

#append/to add contents without replacing existing contents

file=open("demo.txt", 'a')
file.write("am anish")
file.close()