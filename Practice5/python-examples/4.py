import re

text = "Hello World Python TEST"

pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))