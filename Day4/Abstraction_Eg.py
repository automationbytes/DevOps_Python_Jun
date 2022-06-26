from abc import ABC

class car(ABC):
    def mileage(self):
        pass

class Ford(car):
    def mileage(self):
        print("Ford method")


#take

class BMW(car):
    def mileage(self):
        print("BMW method")


c = BMW()
c.mileage()



#take 3 student information from object and print the grades