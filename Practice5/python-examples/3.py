import re

text = "hello_world Test_case another_example"

pattern = r"[a-z]+_[a-z]+"

print(re.findall(pattern, text))