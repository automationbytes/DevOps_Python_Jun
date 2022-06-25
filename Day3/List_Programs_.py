#largest number from a list
#[22:01] DevLabs Trainer - Vignesh - 9941625522 - phone


numlist = [1,7,4,-6]
# numlist.sort(reverse=True)
# print(numlist[0])

#using loop
max1 = numlist[0]
for n in numlist:
    if n > max1:
        max1 = n
print(max1)

#Remove duplicate values from a list

alist = [10,20,30,40,10,20,50,60]
newlist = []
for i in range(len(alist)):
    for j in range(i+1,len(alist)):
        if alist[i] == alist[j]:
          newlist.append(alist[j])
print(newlist)

dup = set(alist)
print(list(dup))


#colors = ['Red','Green','Yellow','Orange','Black','White']
#print all the odd index

#sum of list items numlist = [5,7,9,5,1,7,4,6,4]

#find only matching values from two list
a = [1,7,9,5]
b = [9,1,5,7]
if len(a) == len(b):
    a.sort()
    b.sort()
    if (a==b):
        print("equal")
else:
    print("not equal")


a = [1,7,9,5]
b = [4,3,2,5]
print(set(a).intersection(set(b)))
print(set(a) & set(b))

print([i for i,j in zip(a,b) if i == j]) #list - using lamda

#Find max and min in given set
a1= {1,7,9,5}
z = min(a1)
y = max(a1)
print(z)
print(y)
