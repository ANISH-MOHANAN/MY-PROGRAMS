def division(a,b):
    try:
        return (a/b)
    except:
        print("division error")
        return 0
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
print(division(a,b))


# def division(a,b):
#     try:
#         print(a/b)
#     except:
#         print("division error")
# a=int(input("enter value of a: "))
# b=int(input("enter value of b: "))
# division(a,b)
