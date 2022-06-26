from datetime import datetime

currenttime = datetime.now()
print(currenttime.strftime("%a")) #Sun
print(currenttime.strftime("%A")) #Sunday

print(currenttime.strftime("%d")) #month day
#month
print(currenttime.strftime("%b")) #jun
print(currenttime.strftime("%B")) #june
print(currenttime.strftime("%m")) #06
#years
print(currenttime.strftime("%y")) #22
print(currenttime.strftime("%Y")) #2022

#Hours
print(currenttime.strftime("%H"))#0-24

print(currenttime.strftime("%I"))#0-12

#Min

print(currenttime.strftime("%M"))#00-60

#Sec
print(currenttime.strftime("%S"))#00-60

