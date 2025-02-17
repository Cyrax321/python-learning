num = input("enter a number: ")
num = int(num)

if num % 2 == 0:
    num = "even"
else:
    num = "odd"
print("The number is ->", num)