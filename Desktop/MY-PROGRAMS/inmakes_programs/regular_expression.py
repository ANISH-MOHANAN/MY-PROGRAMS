import re
pattern="python"

if re.match(pattern,"python how are u"):
    print("match found")
else:
    print("match not found")

# #if pattern we trying to match comes first in the content then only match keyword works
# import re
# pattern="python"
#
# if re.match(pattern,"hellopython how are u"):
#     print("match found")
# else:
#     print("match not found")