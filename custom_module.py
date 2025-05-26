def add(x,y):
    return   x + y
#print(add(3,4))

def square(x):
    return x*x
#print(square(5))

def subtract(a,b):
    try:
        result = a - b
    except TypeError:
        return('Cannot accept string arguments, only numbers')
    else:
        print(result)
#print(subtract('c' , 'd'))

def divide(x, y):
    return x/y