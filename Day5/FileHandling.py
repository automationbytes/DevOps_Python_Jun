'''
read "r"
write "w"
append "a "
create "x"
close
delete
'''
import traceback

file1 = open("samplefile.txt","w")
file1.write("Hello\n")
#file1.writelines("This is sample program to add values to file \n File Handling in Python")
li = ["This is sample program to add values to file \n", "File Handling in Python"]
file1.writelines(li)
file1.close()


try:
    file1 = open("samplefile.txt","a")
    file1.write("\nSaturday \n")
except:
    traceback.print_exc()
finally:
    print("hel")
   # file1.close()

file1.write("covid")

try:
    file1 = open("samplefile.txt","r")
    print(file1.read())
except:
    traceback.print_exc()
finally:
    print("h")
    file1.close()

with open("samplefile1.txt","w") as file2:
    file2.write("Hello\n")
    # file1.writelines("This is sample program to add values to file \n File Handling in Python")
    li = ["This is sample program to add values to file \n", "File Handling in Python"]
    file2.writelines(li)
   # file2.close()
