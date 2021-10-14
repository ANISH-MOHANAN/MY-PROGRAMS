#displaying items from a list into a new string at the order we specifies and how many to display
list1=[10,20,30,40]
new_string="my numbers:{0}, {1}, {2}".format(list1[1], list1[3], list1[0])
print(new_string)