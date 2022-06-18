a = 10
b = 50

if a > b:
    print("A is greater than B")
else:
    print("B is greater than A")

############################
a = 8
b = 15
c = 4

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
#elif c>a and c>b:
else:
    print("C is greater")


#normal
a = 100
b = 50

if a > b:
    print("A")
else:
    print("B")
#short hand if-else
print("A") if a>b else print("B")

#short hand if
if a>b: print("A")

q = 33
if(q>10):
    print("Q is above 10")
    if(q>20):
        print("Q is above 20")
        if(q>30):
            print("Q is above 30")


if (q>2):
    pass

a = 10
b = 10
print("A is greater than B" if a>b else "A is equals to B" if a==b else " B is greater")

if (a>b):
    print(" A is greater")
elif(a<b):
    print("B is greater")
else:
    print("A is equals to B")

######
'''
numbers are even or odd with postive or negative
marklist 
a+b+c = sum
get percentage
if percentage greater than r equl80 -> A grade
50-79 - B
rest - C 
'''

print("Enter three number")
a,b,c = input(), input(), input()
print(a)
print(b)
print(c)
