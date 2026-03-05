import re

text = "helloWorldExample"

result = re.sub(r"([A-Z])", r"_\1", text).lower()

print(result)