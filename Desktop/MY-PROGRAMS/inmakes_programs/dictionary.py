# x={"chair":500, "table":300, 34:"python"}
# print(x)

# x={
#     "chair":500,
#     "table":300,
#     34:"python"
# }
# print(x)

# #if key duplication comes the initial value will be replaced with the second one
# x={
#     "chair":500,
#     "table":300,
#     "chair":"python"
# }
# print(x)



# x={
#     "chair":500,
#     "table":300,
#     34:"python"
# }
# print(x)
#
# print(x["chair"])
# print(len(x))

# #to add any item to a existing dictionary
# x={
#     "chair":500,
#     "table":300,
#     34:"python"
# }
# x["veg"]=200
# print(x)
#
# #or we can use update method to add any item to a existing dictionary
# x.update({12:"django"})
# print(x)
#
# #to remove use pop
# x.pop("table")
# print(x)
#
# #or use del
# del x["chair"]
# print(x)

#to print the key in dictionary
x={
    "chair":500,
    "table":300,
    34:"python"
}
# for i in x:
#     print(i)
#
#to see only values in dictionary
for i in x.values():
    print(i)

#to see both key and values using for loop
for i in x.items():
    print(i)