
class Person:

 def __init__(self, name, address, age, id):
    self.name = name
    self.address = address
    self.age = age
    self.id = id
    
 def showDetails(self):
   print(f"Person Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id}")