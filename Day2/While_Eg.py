i = 1
while i<=10:
    print(i)
    if i == 5:
        break

    i+=1

j = 1
while j<=10:
    j += 1

    if j == 5:
        continue
    print(j)

######################################

num = 1234 #4321
reversednum = 0
# numstr = str(num)
# print(type(numstr[::-1]))

while num > 0:
    remainder = num % 10 #4#3
    reversednum = reversednum * 10 + remainder #4 #40+3 #430+2
    num = num//10

print(reversednum)
print(type(reversednum))
