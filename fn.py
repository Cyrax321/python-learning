def say_hello():
    print("HelLo baby girl,how yo doing")
say_hello()

def greet(name):
    print("Hello," + name + "!")
greet("theertha")
greet("abhishek")
greet("Afin")

x = "awesome"
def myfunc1():
    print("python is " + x)
myfunc1()

def myfun2():
    global y
    y= "awsome"
myfun2()
print("IM " + y)

z = "awsome"
def ftn():
    z = "fantastic"
ftn()
print("python is  "+ z)
 #the awesome gets printed cause its defined outside making it as a global variable and the inside defined one gets ignored cause its termed to be local