#Can you add one more method to the class that uses the private attribute?
#Also, please create a new class to demonstrate the use of the public and protected attributes.
#See attached file. See slide 3 : 

class Student:
   def __init__(self, name, age):
        self.name = name # public​
        self._age = age # protected​
        self.__grade = 'A' # private​
        self.__score = 55 # private


   def get_grade(self):
    return self.__grade

   def get_getScore(self):
    return self.__score

   def set_Score(self, score):
       if isinstance(score, (float, int)) and score > 0:
          self.__score = score
       else : print("Your score is too low to set.")
       
class ScienceStudent(Student):
    def show_age(self):
     print(f"age is {self._age}") # accessing protected attribute
    
    def show_name(self):
        print(f"name is {self.name}")  # accessing public attribute
 
s = Student('Ali', 20)

print(s.name) # accessible​

print(s._age) # discouraged​

print(s.get_grade()) # correct way​
s.set_Score(0)

print(s.get_getScore()) # getting score
print("===================>>>>>")
c = ScienceStudent("Charlie1", 30) # changing the value of protected variable age.
c.show_age()
c.show_name()