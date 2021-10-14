#create demo file write random data

file=open("demo1.txt",'w')
file.write("i am anish")
file.close()

#  #open file read contents and display
#
# file=open("demo1.txt",'r')
# content=file.read()
# print(content)
# file.close()
#
# #add new contents without removing the exixting data
#
# file=open("demo1.txt", 'a')
# file.write('\n')
# file.write("and am studying python")
# file.close()

# another way to add new contents without removing the exixting data

file=open("demo1.txt", 'a')
file.write("\nand am studying python \n")
file.close()