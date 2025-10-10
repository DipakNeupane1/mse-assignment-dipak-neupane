# Week 2 - Activity 6 : Develop a basic HR project using OO
# You are tasked with developing a simple program for the Human Resources (HR) department to store
# and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.
# Upload your completed project to GitHub and share the repository link by Friday, 15.8.25, 11:59 PM.


class Employee:

    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}, Job Title: {self.job_title}"

    def give_raise(self, raise_amount):
        initial_salary = self.salary
        self.salary += raise_amount
        print(
            f"Amount {raise_amount} is added into {self.name}'s existing salary, and your updated salary is :: {self.salary} which was {initial_salary} before the raise."
        )


if __name__ == "__main__":

    employee_one = Employee("Dipak Neupane", 2000, "Senior Software Engineer")
    print(
        f"{employee_one.name.split()[0]}'s employment details are :: {employee_one.display_info()}"
    )

    # Raise first employee's salary by 20.
    employee_one.give_raise(20)
    print(
        f"After the raise, {employee_one.name.split()[0]}'s employment details are :: {employee_one.display_info()}"
    )

    employee_two = Employee("Bhuwan Bhatt", 3000, "Senior Cloud Architect")
    print(
        f"{employee_two.name.split()[0]}'s employment details are :: {employee_two.display_info()}"
    )

    # Raise second employee's salary by 30.
    employee_two.give_raise(30)
    print(
        f"After the raise, {employee_two.name.split()[0]}'s employment details are :: {employee_two.display_info()}"
    )
