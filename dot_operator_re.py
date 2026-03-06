import re

text = "aa b aaaa"

result = re.findall(r"a*", text)
print(result)