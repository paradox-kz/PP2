import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

for emp in data["employees"]:
    print(emp["name"], emp["age"])
