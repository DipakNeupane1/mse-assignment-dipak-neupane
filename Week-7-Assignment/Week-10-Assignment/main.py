"""The purpose of this Main class is to run some calculations on users input string."""
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
