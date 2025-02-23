#WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS HINT: A PALINDROME IS A WORD THAT IS SPELLED THE SAME WAY BACKWARDS AS IT IS FORWARDS, USE COPY() METHOD 

# TO CREATE A COPY OF THE LIST AND THEN USE REVERSE() METHOD TO REVERSE THE LIST AND THEN COMPARE THE TWO LISTS TO CHECK IF THEY ARE EQUAL OR NOT

list = []
list.append(input("enter the first element: "))
list.append(input("enter the second element: "))
list.append(input("enter the third element: "))
list.append(input("enter the fourth element: "))

list1 = list.copy()
list1.reverse()

if list == list1:
    print("the list is a palindrome")
else:
    print("the list is not a palindrome")




# OUTPUT:   

# enter the first element: 1
# enter the second element: 2
# enter the third element: 3
# enter the fourth element: 4
# the list is not a palindrome

# OUTPUT:

# enter the first element: 1
# enter the second element: 2
# enter the third element: 2
# enter the fourth element: 1
# the list is a palindrome