# Week 5 - activity 2: Develop a Python program that demonstrates the usage of inheritance
# Review the attached file and develop code that demonstrates the use of inheritance as a core feature in your OOP implementation.
# Upload your code to GitHub and share the repository link, including a short comment that explains your understanding.
from person import Person


class Academic(Person):

    def __init__(self, name, address, age, id, tax_code, salary):
        super().__init__(name, address, age, id)
        self.tax_code = tax_code
        self.salary = salary

    def showDetails(self):
        print(
            f"Academics: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id}, Tax Code: {self.tax_code}, Salary: {self.salary}"
        )

    def greet(self):
        print("Greetings and felicitations from the maestro " + self.name)
