import re

txt = "Hello126World"
#a = re.findall("[0-9]",txt)
a = re.findall("\d",txt)
print(a)
b = "".join(a)
print(b)

#to extract char

c = re.findall("\D",txt)
print(c)
d = "".join(c)
print(d)

#remove unwanted spaces
str = "   Hi    world   "
q = re.sub('\s',"",str)
print(q)

txt = "Hello126World"
w = re.sub('\d',"",txt)
print(w)