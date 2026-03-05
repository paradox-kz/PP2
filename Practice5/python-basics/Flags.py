import re
print(re.findall(r"hello", "Hello HELLO", re.IGNORECASE))
text = "Hello\nWorld"

print(re.findall(r"^World", text, re.MULTILINE))