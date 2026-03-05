import re

text = "My phone number is 12345"

result = re.search(r"\d+", text)

print(result.group())