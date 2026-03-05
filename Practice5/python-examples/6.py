import re

text = "Hello, world. Python regex"

result = re.sub(r"[ ,\.]", ":", text)

print(result)