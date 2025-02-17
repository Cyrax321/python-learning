#nesting of if statements

age = input("enter your age: ")
age = int(age)
if age>18:
    if age >80:
        print("you are too old to drive")
    else:
        print("you can drive")
else:
    print("you cannot drive")