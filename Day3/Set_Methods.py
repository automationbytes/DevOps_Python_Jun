#add - can be added in any position (closest comparision to list append)
fruits = {"Apple","Banana","Mango","Grapes","Banana"}
fruits.add("Orange")
print(fruits)

#update - add two sets (Closest extend in list)
fruits = {"Apple","Banana","Mango","Grapes"}
newfruits = ["Stawberry","Blueberry","Orange","Banana"]
fruits.update(newfruits)
print(fruits)

#remove

#pop - it will remove any value from a set
#fruits.pop()
print(fruits)

#remove - remove specified value from set; it will error when value is not there
fruits.remove("Apple")
print(fruits)

#discard - same lik remove, only diff it will not throw any error
fruits.discard("Mango")
print(fruits)

#fruits.remove("Devops")
print(fruits)

#clear - removes all the values from the set
newfruits =fruits.copy()
newfruits.clear()
print(newfruits)

a = {}# dict
print(type(a))

b = set()
print(type(b))

#del
del (newfruits)
#print(newfruits)


#intersection - gives common values

fruits = {'Grapes', 'Apple', 'Orange', 'Banana'}
company = {'Google','Apple','Orange','Microsoft'}
operationsystem = {"Microsoft","Apple"}
print(fruits.intersection(company)) # it will not affect our set values.
print(fruits)

fruits.intersection_update(company) # it will update the result to the first set
print(fruits)
print(company)


fruits = {'Grapes', 'Apple', 'Orange', 'Banana'}
company = {'Google','Apple','Orange','Microsoft'}
operationsystem = {"Microsoft","Apple"}
print(fruits.intersection(company,operationsystem))


#sym diff
print(fruits.symmetric_difference(company))

#union
print(fruits.union(company) , "union")
print(fruits , "printing fruits")


#update - add two sets (Closest extend in list)
a = {"Apple","Banana","Mango","Grapes"}
b = {"Stawberry","Blueberry","Orange","Banana"}
a.update(b)
print(a,"printing after update")

a = {1,2,3}
b = {4,5,2}
print(a.union(b))
print(a)

#update
#a.update(b)
print(a)

#diff - unique values of a
print(a.difference(b)) #unique values of a will be printed
print(b.difference(a)) #unique values of b will be printed

x = {1,7,9,5,6,3}
y = {1,3}
#superset - returns if all the values of set2 is present in set1
print(x.issuperset(y))

#subset - reverse of superset
print(y.issubset(x))


#isdisjoint - returns true if both doesnt hav common values
x = {1,7,9,5,6,3}
y = {1,3}

z = {10,15}
print(x.isdisjoint(z))
print(x.isdisjoint(y)) #false - since it has common values

