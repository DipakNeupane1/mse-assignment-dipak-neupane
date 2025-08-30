from student import Student
from person import Person
from academics import Academic
from general_staff import GeneralStaff

class Main():
    
    def create_obj(self):
       # Here the base class is person and student,generalstaff,and academics are child classes 
       # which inherits the properties of base class person and can have their own specific properties as well.
       #This is an example of inheritance, which reduces the code duplication and makes our code much robust and clean.
        person = Person("Charlie","21 whitaker place",20,"ID")
        person.showDetails()
        student = Student("Charlie","21 whitaker place",20,"ID","pass")
        student.showDetails()
        academics = Academic("Charlie","21 whitaker place",20,"ID","tax_code",1000)
        academics.showDetails()
        general_staff = GeneralStaff("Charlie","21 whitaker place",20,"ID",23.51)
        general_staff.showDetails()
    
if __name__ == "__main__":
 main_app = Main()
 main_app.create_obj()