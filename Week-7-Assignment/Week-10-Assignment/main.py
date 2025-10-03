#Week 10 - Activity 1: Use Pylint
#Develop an Object-Oriented (OO) Python project that reads either a string or a list, then performs two analyses:
#Calculates the total length.
#Determines the number of uppercase characters.
#The project should be structured with appropriate classes and methods. After implementation, use Pylint to analyze and improve the code quality, ensuring adherence to Python’s best practices and style guidelines. Share the result when you have done.

class Main:
    """This class have two methods one for calculating total number of length 
    in given string and another for finding numbers of uppercase chrs in given string """
    def calculate_total_length(self, val):
        """determines the total length of chrs in given string."""
        return len(val)
    def determine_number_of_total_uppercase_chr(self, val):
        """determines the uppercase chr in given string."""
        return sum(1 for ch in val if ch.isupper())

if __name__ == "__main__":
    main_app = Main()
    print(main_app.calculate_total_length("dipak"))
    print(main_app.determine_number_of_total_uppercase_chr("Dipak"))
