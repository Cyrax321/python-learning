info = {
    "name" : "john",
    "age" : 25,
    "marks" : [94.4,87.5,95.2,66.4,45.1]
    }

print (info)

print(info["name"])
print(info["age"])
print(info["marks"])

del info["marks"]
print(info)

for key in info:
    print(key, info[key])