# def addition(a,b):
#     return a+b
# print(addition(20,30))

# #the above code can be simplified using lambda
# x=lambda a,b: a+b
# print(x(20,30))

# x=lambda a : a+30
# print(x(20))

#here b*c is calculated first beacuse * has more precedence
x=lambda a,b,c : a+30+b*c
print(x(20,10,5))

# #this can be done in a complex way
# def fun(n):
#     return lambda b:b+n
# x=fun(2)
# print(x(8))