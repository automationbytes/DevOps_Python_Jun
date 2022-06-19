#String - datatype anything wit single or double quote

a = "Hello"
print(a)
print(type(a))

multiline = '''Python is one the most easiest programming language.
And it support everything.
It run on multiple OS.
'''
print(multiline)

a = "APPLE FRUIT"

#len of string
print(len(a)) #11

#indexing
print(a[7])

#Negative indexing
print(a[-7])

#slicing
print(a[2:5])#ple
print(a[2:])#print till the last value
print(a[:5])#start value is defaulted by 0

#negative slicing - we need provide small number at start position
print(a[-9:-6])#ple
print(a[-9:])#it will goes til the last value
print(a[:-3])

print(a[6:8])

#Strip - used to trim down the white spaces
a = "      Hello     World        "
print(a.strip()) #trim both front and back
print(len(a.strip()))
print(a.lstrip()) #trim only left
print(len(a.lstrip()))
print(a.rstrip()) #trim only right
print(len(a.rstrip()))

#lower case
a = "HEllo woRLD"
print(a.lower())

a = "GRAß" #grass
print(a.lower())
print(a.casefold())

#upper case
print(a.upper())

b = "python is popular language in AI.eventhough we hav other languages like R but python leads the stage"
print(b.capitalize())
print(b.title())
print(b.swapcase())

#Replace
print(b.replace("python","java"))
print(b.replace("i","II"))

#split
wordlist = b.split(" ")
print(wordlist)
print(type(wordlist))
print(wordlist[2])
print(wordlist[-4])

#concat
a = "hello"
b = 5
c = a+str(b)
d = a+format(b)
print(c)
print(d)

a = "Apple is a fruit. Also apple is phone"
print(a.startswith("Apple"))

print(a.endswith("Apple"))

#count
print(a.count("p"))
print(a.count("p",5))


a = "apple"
c = a.center(30)
print(len(c))

d = "GRAß".encode()
print(d)

str = "All string methods returns new values.\tThey do not change the original string"
print(str.expandtabs(4))
print(str.find("They"))#39
print(str[39:])
print(str.find("Python"))
#index
print(str.index("They"))#39
#print(str.index("Python"))

name = "Python18"
print(name.isalnum())#alphabets and numbers

print(name.isalpha())# only alphabets

print(name.isascii())#only english letter
a = "GRAß"
print(a.isascii())

pi = "314"
print(pi.isdigit()) #int value

fruits = ["apple","banana","stawberry"]
print(type(fruits))
x = " ".join(fruits)
print(type(x))
print(x)
print(fruits)


str = "All string methods returns new values.\nThey do not change the original string"
print(str)
sp = str.splitlines(True)
print(sp)

accountnum = "45679"
print(accountnum.zfill(16))
print(accountnum)