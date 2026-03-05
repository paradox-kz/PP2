import re

text = "a ab abb abbb ac"

pattern = r"ab*"

print(re.findall(pattern, text))