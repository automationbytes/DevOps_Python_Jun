'''
try - test the block of code with errors/may contains error
except - block used to handle errors
finally - irrespective of the results finally will be executed. used to handle clean-up codes
else - no errors occured in try block (optional)

'''

# normal try and except
import traceback

try:
    print("Hello")
except:
    print("An exception occured")

#when error/exception occured

try:
    print(a)
except:
    print("An exception occured")
    #traceback.print_exc() # used to print the exception
    traceback.print_exc()

#Multiple Exception
#when error/exception occured

try:
    print(10/0)
except NameError:
    print("Variable a is not defined")
except:
    print("An exception occured","multiple error")
    #traceback.print_exc() # used to print the exception
    traceback.print_exc()

#finally
try:
    print("abc")
except:
    print("Except block")
finally:
    print("Finally block")


#else
try:
    print(abc)
except:
    print("Except block")
else:
    print("Else part")

#raise keyword - to create user defined exception
age = 5
if age < 18:
    raise Exception("Sorry, not eligible")