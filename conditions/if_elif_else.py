age=input("enter your age:")
age=int(age)
if(age<18):
    print("you are not eligible to vote")
    print("you are a minor")
elif(age>=18):
    print("you are eligible to vote")
    print("you are a major")
else:
    print("invalid input")