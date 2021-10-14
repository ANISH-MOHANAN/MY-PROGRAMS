# result=[]
# for i in "inmakes":
#     result.append(i)
# print(result)

# #above program simplified using list comprehensive
# result=[i for i in "inmakes"]
# print(result)


# #to print words starts with p into a new list
# result=["python","django","flask","people"]
# new=[]
# for i in result:
#     if 'p' in i:
#         new.append(i)
# print(new)

# #above program simplified using list comprehensive
# result=["python","django","flask","people"]
# new=[i for i in result if 'p' in i]
# print(new)

# #range
# new=[i for i in range(10)]
# print(new)

# #to print a word instaed of items in list
# result=["python","django","flask","people"]
# new=["hello" for i in result]
# print(new)

# #to make items in list to upper case
# result=["python","django","flask","people"]
# new=[i.upper() for i in result]
# print(new)

#to multiply numbers in list
num=[1,2,3,4]
new=[i*i for i in num]
print(new)