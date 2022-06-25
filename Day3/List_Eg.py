'''
List is very similar to arrays in other languages
It is mutable(modifiable)
Ordered - Insertion order
List allows duplicate values/elements
[] - used for storing values
Hetrogeneous - It can contain both similar and different data types
elements will be calculated based on index values
'''


fruits = ["Apple","Banana","Mango","Grapes","Banana"]
print(fruits)
#length of list
print(len(fruits))

#indexing (starts from 0)
print(fruits[0])

fruits[4] = "Mango"
print(fruits)

#negative indexing (from the last value)
print(fruits[-2])

#Slicing - cuting down the list into small list
#['Apple', 'Banana', 'Mango', 'Grapes', 'Mango']
print(fruits[1:4])

#start from 2 and print till the end
print(fruits[2:])

#start from first and slice at some point
print(fruits[:3])

#Negative slicing
print(fruits[-5:-2] , "Negative slicing")
print(fruits[:-1])
print(fruits[-3:])

#using for loop
vegetables = ["Onion","Tomato","Potato","Carrot","Beetroot"]
for i in range(0,len(vegetables),1):
    print(vegetables[i])
print("*******************")
#for each loop - using membership operator
for v in vegetables:
    print(v)
    if v=='Potato':
        print("Potato is available")
        break

mixedlist = [1,"Hello",5.5,"World"]
print(mixedlist)