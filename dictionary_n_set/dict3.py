null_dict = {}
null_dict["name"] = "john"
null_dict["age"] = 25
print(null_dict)

#nested dictionaries

student = {
    "name" : "john",
    "age" : 25,
    "subjects" : ["physics","chemistry","maths","biology","english"],
    "scores" : {
        "physics" : 94.4,
        "chemistry" : 87.5,
        "maths" : 95.2,
        "biology" : 66.4,
        "english" : 45.1
    },
    "is_adult" : True,
    "is_student" : False
}

print(student["name"])
print(student)

print(student["scores"])
