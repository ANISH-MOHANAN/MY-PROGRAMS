import re
pattern="[A-Z][0-9][a-z]"

if re.search(pattern,"P7s"):
    print("match found")
else:
    print("no match found")


# #if we give wrong string
# import re
# pattern="[A-Z][0-9][a-z]"
#
# if re.search(pattern,"sP7"):
#     print("match found")
# else:
#     print("no match found")

