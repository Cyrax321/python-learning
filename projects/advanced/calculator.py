print("--------------------------------------------------------")
a=float(input("Enter the first number  : "))
b=float(input("Enter the second  number: "))
print("You have entered first number as  -> ",a)
print("You have entered second number as -> ",b)

print("Select the operation")
print(" \n 1.Addition \n 2.Subsraction \n 3.Multiplicaation \n 4.Division \n 5.Square \n ")

n = int(input("Enter the operation number: "))

if n==1 :
    s=(a+b)
    print("The addition result is: ",s)
elif n==2 :
    t=(a-b)
    print("The substraction result is: ",t)
elif n==3:
    u=(a*b)
    print("The multiplication result is: ",u)
elif n==4:
    v=(a/b)
    print("The division result is: ",v)
else:
    w=float(a**b)
    print("The square of the number is: ",w)

print("--------------------------------------------------------")


#                        **sample output**

#   --------------------------------------------------------
#   Enter the first number  : 1
#   Enter the second  number: 1
#   You have entered first number as  ->  1.0
#   You have entered second number as ->  1.0
#   Select the operation
 
#   1.Addition 
#   2.Subsraction 
#   3.Multiplicaation 
#   4.Division 
#   5.Square 
 
#   Enter the operation number: 2
#   The substraction result is:  0.0
#   --------------------------------------------------------