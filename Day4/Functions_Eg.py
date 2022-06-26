'''
Functions (Methods) - Block of code which will be executed only when its called
parameterizing
returning value
reusability


def functioname(anyparameter):
    return statement

def - def key word used for declaring a function

'''

def sum(a,b):
    return a+b

c = sum(8,10)%5
print(c)


#if we dont knw exact input
def myfun (*any):
    print("Print values",any[2])
myfun("ab","cv","xuy","po")

def myfunct (**sum):
    print (sum["a"] + sum["b"])

myfunct(a = 10, b = 5)

def mysum (a = 10,b = 5):
    print (a+b)

mysum(5,19)#24
mysum()
print("*****************")

#lambda
add = lambda a,b: a+b
print(add(10,5))