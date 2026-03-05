import re

text = "a123b axxb ab acb"

pattern = r"a.*b"

print(re.findall(pattern, text))