a=int(input('Enter the First Number:\t'))
b=int(input('Enter the Second Number:\t'))
c=int(input('Enter the Third Number:\t'))
if a>b and b>c:
   print(a)
elif b>c and b>a:
   print(b)
else:
   print(c)