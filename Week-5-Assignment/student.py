from person import Person


class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        super().__init__(name, address, age, id)
        self.academic_record = academic_record

    def showDetails(self):
        print(
            f"Student Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id}, Academic Record: {self.academic_record}"
        )

    def greet(self):
        print("Greetings and felicitations from the maestro " + self.name)
