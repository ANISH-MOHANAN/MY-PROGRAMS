# li=[1,2,3,4,5,6,7,8]
# li2=[i for i in li if i%2==0]
# print(li2)

# string1=["python","java","programming","confused"]
# newlist=[]
# for i in string1:
#     if 'p' in i:
#         newlist.append(i)
# print(newlist)

# #this is just a try to do it using index method
# string1=["python","java","programming","confused"]
# print(string1[1:4])

# #code using list comprehensive method
# string1=["python","java","programming","confused"]
# new_string=[i for i in string1 if 'p' in i]
# print(new_string)

# correct code using string formatting
string1=["python","java","programming","confused"]
new_string="my string: {0}, {1}, {2}".format(string1[1], string1[3], string1[0])
print(new_string)

