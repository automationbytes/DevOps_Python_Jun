'''
Object Oriented programming

Student

#attributes
	name
	age
	rollnum

#behavior
	learningpython()
	attendingclass()

'''


class Student:
    name = "Tom"
    age = 10

    def readmethod(self):
        print(self.name, "'s read method ")


s = Student()
s.readmethod()
''''
*****************************************
'''


class StudentwitCon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def readmethod(self):
        print(self.name, "'s read method ")


s = StudentwitCon("jerry",5)
s.readmethod()


class animal:
    def eat(self):
        print("Animal eat method")
class Dog(animal):
    def bark(self):
        print("Dog bark method")

    def eat(self):
        print("Dog's veg method")

d = Dog()
d.eat()
d.bark()


#overriding

class marriageproposal:
    def partnerchoosing(self):
        print("XYZ")

    def gift(self):
        print("House")

class childdecision(marriageproposal):
    def partnerchoosing(self):
        print("abc")

c = childdecision()
c.gift()
c.partnerchoosing()