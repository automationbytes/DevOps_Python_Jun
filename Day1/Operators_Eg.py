#Operators - to operations on variables and values

'''
Arithmetic Operators - Numeric operations like addition/sub
Assignment Operators
Comparison Opertors
Logical Operators
Identity Operator (is)
Membership Operator (in)
Bitwise Operator

'''

#Arithmetic Operators - Numeric operations like addition/sub

a = 10
b = 3

print(a+b)# + arthimetic operator // 14
print(a-b)
print(a*b)
print(a/b)
print(int(a/b))
print(a//b) # returns quotient and called as floor division
print(a%b) #return remainder and called as modulas
print(a**b) #exponential

#Assignment - assign back the values to the variables
a = 5
#a = a+3 #8
a += 3 #a=a+3
print(a)
a -= 2
print(a)

#Comparison Operator - compare and return true or false

'''
== - equals to
!= - not equals to
> - Greater than
< - Lesser than
>= - Greater than or equal to
<= - lesser than or equal to
'''

a = 10
b = 5
print(a >= b)
print(a<b)

#Logical Operators - combine 2 statements

'''
and
true and true = true
true and false = false
false and true = false
false and false = false

or

True or True = True
True or False = True
False or True -= True
False or False = False

not - reverse our result
False -> True
True -> False

'''

a = 10
b = 5
c = 8
print(a>b)
print(a>c)
print((a<b) and (a>c)) #false and true -> false
print((a<b) or (a>c))#false or true-> true

print(not(a<b))

#Bitwise Operator - COnvert into Binary and compare
'''
& - And
| - or
~ - Not

And 
1 and 1 = 1
1 and 0 = 0
0 and 1 = 0
0 and 0 = 0

or
1 or 1 = 1
1 or 0 = 1
0 or 1 = 1
0 or 0 = 0

'''

a = 10 #1010
b = 3  #0011
#-------0010 # 2 -> and
#=======1011->8+0+2+1=>11
print(a & b)
print(a | b)


#Identity Operator -> is and not is -> check both values belongs to same memory
x = ["apple","ball"]
y = ["apple","ball"]
z = y
print(x)
print(y)
print(z)

print(x is y) # False - Not belongs to Same Object
print(y is z) # True - it belongs to same object
print(x == y) #just check values - ttue

#Membership - test whether the values present in given list/set/tuple

x = ["apple","ball","car","dog"]
print("car" in x) #true
print("elephant" not in x)
