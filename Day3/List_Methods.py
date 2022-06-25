#Add any values to list
fruits = ["Apple","Banana","Mango","Grapes","Banana"]
vegetables = ["Onion","Tomato","Potato","Carrot","Beetroot"]

#append - at the end of the list
fruits.append("Orange")
print(fruits)

fruits.append(vegetables)
print(fruits) # adding list is also possible. it will be treated as sublist
print(fruits[6])
print(fruits[6][3])#accessing inner list (sublist)

fr = ['Apple', 'Banana', 'Mango', 'Grapes', 'Banana', 'Orange', ['Onion', 'Tomato',[ 'Potato', 'Carrot'], 'Beetroot']]

#extend
fruits = ["Apple","Banana","Mango","Grapes","Banana"]
vegetables = ["Onion","Tomato","Potato","Carrot","Beetroot"]

fruits.extend(vegetables)
print(fruits)

fr = ['Apple', 'Banana', 'Mango', 'Grapes', 'Banana', 'Orange', ['Onion', 'Tomato',[ 'Potato', 'Carrot'], 'Beetroot']]
print(fr[6])
print(fr[6][2])
print(fr[6][2][0])

set1 = {1,5,9,7,5}
print(set1)
fruits.extend(set1)
print(fruits)

#insert
vegetables = ["Onion","Tomato","Potato","Carrot","Beetroot"]
vegetables.insert(2,"Beetroot")
print(vegetables)

numlist = [1,5,9,7,7,8]
numlist.insert(4,4) #list.insert(position,value)
print(numlist)

#copy
newveg = vegetables.copy()
print(newveg)
print(vegetables)

newveg1 = vegetables
print(newveg1)

#clear
newveg1.clear() #only values will be cleared(deleted), variable will be thr
print(newveg1)

#delete
del(newveg1) #delete keyword used to delete the list itself
#print(newveg1)

#count - number of elements with specified value
print(newveg.count("Beetroot"))

print(newveg.count("Apple"))

fr = ['Potato', 'Banana', 'Mango', 'Grapes', 'Banana', 'Orange', ['Potato', 'Tomato',[ 'Potato', 'Carrot'], 'Beetroot']]
print(fr.count("Potato"))

#index - provides the index of particular value - always provide the first occurence
fruits = ['Potato', 'Banana', 'Mango', 'Grapes', 'Banana', 'Orange','Grapes']
print(fruits.index("Grapes"))
#if the value not there, it will throw error
#print(fruits.index("Onion"))

#pop - used to remove the last value
print(fruits)
fruits.pop()
print(fruits)
#pop with index - it will remove value on specified index
fruits.pop(3)
print(fruits)

#remove - removes the first matching value from the list
fruits.remove('Banana')
print(fruits)
#fruits.remove("12654")

#sorting list in ascending or descending order
alphabets= ["Apple","Zebra","cat","cow","kal","#"]
alphabets.sort() #reverse= false by default
print(alphabets)

#to sort in descending order
alphabets.sort(reverse=True)
print(alphabets)

a = ['Potato', 'Banana', 'Mango', 'Banana', 'Orange']
a.reverse()
print(a)