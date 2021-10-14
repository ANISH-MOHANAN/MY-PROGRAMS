#search keyword finds the pattern to be searched even the pattern is located anywhere
import re
pattern="python"

if re.search(pattern,"hello am python programmer,how are u? are u fast?"):
    print("pattern matched")
else:
    print("pattern not found")

