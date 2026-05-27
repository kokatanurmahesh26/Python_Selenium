#constructor class
class student :
    def __init__(self, name, age):
        self.name = name #instance variable used at the time of object creation
        self.age = age

    def display(self) :
        print(self.name)
        print(self.age)

s1 = student("mahesh", 29) #triggering the constructor by initializing/instantiating class 
s1.display()
