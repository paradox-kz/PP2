import re

text = "My age is 25"

result = re.search(r"\d+", text)

print(result.group())