x=("a","b","c","d","e","f","g")
y=list(x)

#inserting
y.insert(7,"h")
print(y)

#append
y.append("i")
print(y)

#to find index of second element from last position
print(y[-2])

#now convert list back to tuple
x=tuple(y)
print(x)