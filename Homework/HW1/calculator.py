def add(x, y, z):
    return int(x)+int(y)+int(z)
    
def sub(x, y, z):
    return int(z)-int(y)-int(x)
    
def mult(x, y):
    return int(x)*int(y)
    
def div(x, y):
    return int(x)/int(y)
    
x = input("Enter an integer: ")
y = input("Enter an integer: ")
z = input("Enter an integer: ")

print("(x+y+z)*x/(z-y-x)*y) =", div(mult(add(x,y,z), x), mult(sub(x,y,z), y)))
