#dictionary is mutable 
#don't allow duplicate key

dict ={
    "name" : "john",
    "age" : 25,
    "marks" : [94.4,87.5,95.2,66.4,45.1],
    "subjects" : ["physics","chemistry","maths","biology","english"],
    "is_adult" : True,
    "is_student" : False
}

print(dict["name"])
print(dict["age"])
print(dict["marks"])
print(dict["subjects"])
print(dict["is_adult"])
print(dict["is_student"])
print(dict)

dict["name"] = "anandhu" #overwrites the value of the key "name"
dict["surname"] = "p"
dict["last nmae"] = "Shaji"
print(dict)

