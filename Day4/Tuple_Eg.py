''''
Tuple - Ordered
and unchangeable
Duplicates are allowed
() - without brackets if we giv multiple values
'''

fruits = ("Apple","Banana","Mango","Grapes","Banana")
print(fruits)

print(fruits[0])
#
# fruits[0] = "Stawberry"
# print(fruits)

#length
print(len(fruits))

#multiple datatypes
multituple = 1,"Abc","xyz",25.6
print(multituple)
print(type(multituple))

#tuple as constructor
veg = tuple(("onion","carrot","cabbage"))
print(veg)
print(type(veg))

#indexing
print(veg[0])
#negative indexing
print(veg[-1])

fruits = ("Apple","Banana","Mango","Grapes","Banana")
print(fruits[1:3])

#update/add/remove - convert to list then we can add/update then change to tuple
#update to tuple
newlist = list(fruits)
newlist[1] = "Stawberry"
fruits = tuple(newlist)
print(fruits)
print(type(fruits))

#Add into tuple
newlist = list(fruits)
newlist.append("Blueberry")
fruits = tuple(newlist)
print(fruits)
print(type(fruits))

#Remove items
newlist = list(fruits)
newlist.remove("Grapes")
fruits = tuple(newlist)
print(fruits)
print(type(fruits))

#unpacking
fruits = ("apple","mango","banana","papayya","blueberry")
(red,*yellow,blue) = fruits
print(red)
print(yellow)
print(blue)

#looping
#forezch
for f in fruits:
    print(f)

#normal forloop
for i in range(len(fruits)):
    print(fruits[i])


#count - how many times values are repeated
fruits = ("apple","mango","banana","papayya","blueberry","apple")
print(fruits.count("apple"))
#index - returns the position of the value
print(fruits.index("apple"))

nefruits = list(fruits)
nefruits.sort()
print(nefruits)
