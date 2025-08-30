from person import Person

class GeneralStaff(Person):
    
 def __init__(self,name, address, age, id, pay_rate):
     super().__init__(name, address, age, id)
     self.pay_rate = pay_rate
     
     
 def showDetails(self):
   print(f"Staff Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id}, Pay Rate: {self.pay_rate}")
   
 def greet(self):
    print("Greetings and felicitations from the maestro "+ self.name)