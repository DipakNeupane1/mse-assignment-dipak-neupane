class Person:

    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id

    def showDetails(self):
        print(
            f"Person Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id}"
        )

    # Week 5 Activity 4: learning about overriding methods
    # Use the attached file to demonstrate method overriding. Update the attached Python code accordingly and share your GitHub link.

    def greet(self):
        print("Greetings and felicitations from the maestro " + self.name)
