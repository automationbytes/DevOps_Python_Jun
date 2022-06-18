'''
Variables always starts with an alphabets or underscore
should not contains any special chars (#,$%^&)
variables should hav any space in between
variables are case sensitive

Datatypes = type of the variable
number - int, float, complex
string - char, string
boolean - true/false

'''
a = 5
A = 10
print(a)
print(type(a))#int
a = "Hello"
print(a)
print(type(a))#String


f = 15.5
print(type(f))#float

#a - variable name
#= - conditional operator
#5 or string - values
'''
number - int(without decimal point), float(with decimal point) and complex (numbers wit real and imaginary)
string
boolean - true/false
list
set
tuple
dict

'''
c = 1+2j
print(type(c))
aa = 498749106489648943218945961981654949874
print(type(aa))
print(aa)
fa = 4987.49106489648943218945961981654949874 #15 digits after tat it will round off
print(fa)

b = True
print(type(b))
#type - return which datatype the variable belongs too
#isinstance- return true,false based on variable we provided
#syntax isinstance(var,datatype)

a = 5.5
print(isinstance(a,complex))
print(isinstance(5.5,(int,float)))

x = None
print(x) #None
print(type(x)) #NoneType

y = b"Hello"
print(y)#b'Hello'
print(type(y))#bytes

z = bytearray(3)
print(z)#\x00
print(type(z))

print(memoryview(bytes(3)))

a,b,c= 10,5,10
print(a)
print(b)
print(c)

a = b = c = 5
print(a)
print(b)
print(c)

#type casting - converting from one datatype to other

a = 5
b = float(a)
print(a)#5
print(type(a))#int
print(b)#5.0
print(type(b))#float
print(int(579.99999999999999))

print(complex(a))#5+0j

a = '5'
print(type(a))
print(type(int(a)))
b = '5a'
print(int(b))