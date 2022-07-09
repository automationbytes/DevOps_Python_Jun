'''
Dict - use key and value pair
 will not hav duplicates key
 3.7 - dict ordered - 3.6 unordered
 changeable
{} - curly brackets
'''

mydict = {
    "fruit" : "Apple",
    "vegetable":"Carrot",
    "language":"Python"
}

print(type(mydict))

#length
print(len(mydict))

#Accessing the elements
#key or get method
print(mydict["vegetable"])
print(mydict.get("fruit"))

#print all the keys
print(mydict.keys())

#print the values
print(mydict.values())

#print as key and value
print(mydict.items())


#for loop for iterating keys
for k in mydict.keys():
    print(k)

#for loop for iterating values
for v in mydict.values():
    print(v)

#iterating both
for k,v in mydict.items():
    print(k,"----",v)

#this will iterate only keys
for x in mydict:
    print(x)
#TO get values
    print(mydict[x])


#Adding items to dict
mydict["color"] = "blue"
print(mydict)

#updating the items in dict
mydict.update({"color":"red"})
print(mydict)

#update the value if not present
mydict.update({"car":"ferrari"})
print(mydict)

mydict = {
    "fruit" : "Apple",
    "vegetable":"Carrot",
    "language":"Python",
    "fruit": "Mango"#update

}
print(mydict)

#setdefault-  if yu hav a key- it wont update; else it wil add
mydict.setdefault("color","blue")
print(mydict)

mydict.setdefault("fruit","orange")
print(mydict)

#pop - removes specified key value

mydict.pop("color")
print(mydict)
#popitem - it removes last value
mydict.popitem()
print(mydict)

#copy
newdict = mydict.copy()
print(newdict,"new dict")

newdict.clear()
print(newdict)

#mydict.values()
#Lab exercises:
#1) Check whether we hav specified key
#2) Find the sum of all the values in the dict
#3) Remove specified key
