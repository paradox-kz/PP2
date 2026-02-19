import json

json_string = '{"name": "John", "age": 30}'

data = json.loads(json_string)

print(data["name"])
print(type(data))  # dict
