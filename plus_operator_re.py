#+ → One or More
import re

text = "aa a aaa aaaa"

result = re.findall(r"a+", text)
print(result)