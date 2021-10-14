# #create list from existing list by the repeating of letters in the elements of the existing list
# string1=["python","java","programming","confused"]
# new_string=[i for i in string1 if i.count('m')>1]
# print(new_string)

#create list from existing list using the count of letters in words in the existing list
string1=["python","java","programming","confused"]
new_string=[i for i in string1 if len(i)>4]
print(new_string)
