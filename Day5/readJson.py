import json

f = open("data.json","r")

data = json.load(f)
print(type(data))
for i in data:
    print (data[i])