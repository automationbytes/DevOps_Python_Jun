#Start, Stop , Step

for i in range(10,100,10):
    print(i)
print("*******************************")
#Start, Stop, step - value is defaulted by 1
for i in range(10,100):
    print(i)
print("*******************************")
#Stop (Start - value is defaulted by 0 and step - value is defaulted by 1)
for i in range(10):
    print(i)


for i in range(10):
    print(i)

print("*******************************")

for i in range(100,0,-10): # Start - 100, stop-0, step -1
    print(i)
    if i == 50:
      #  pass
        break
else:
    print("Loop stopped bcoz of break")
print("*******************************")


for i in range(10,100,10): # Start - 100, stop-0, step -1
    print(i)
else:
    print("END of LOOP")



for i in range(100,0,-10): # Start - 100, stop-0, step -1
    if i == 50:
        continue
    print(i)

else:
    print("Loop stopped bcoz of break")
print("*******************************")

for i in range(1,10,2):
    print(i,"Outer")
    for j in range(1,3,1):
        print(j,"Inner")

