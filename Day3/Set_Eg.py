'''
Set is very similar to list
It is mutable(modifiable)
But its not maintain Insertion order
set will not allows duplicate values/elements
set will not allow indexing (unindexed)
{} - used for storing values
Hetrogeneous - It can contain both similar and different data types
elements will be calculated based on index values
'''

fruits = {"Apple","Banana","Mango","Grapes","Banana"}
print(fruits)
print(type(fruits))
#length - after remving duplicates, it will giv the length
print(len(fruits))

mixedset = {1,"Hello",4.5}
print(mixedset)

#set constructor
newfruits  = set(("Apple","Banana","Mango","Grapes","Banana"))
print(newfruits)
print(type(newfruits))

#for loop
for n in newfruits:
    print(n)
# #normal for loop willnot work here
# for i in range(len(newfruits)):
#     print(newfruits(i))