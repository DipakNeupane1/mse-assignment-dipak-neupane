class StringManipulator:
    # These are instance methods of the class
    def find_character(self, input_string, char):
        return input_string.find(char)
    
    def find_length(self, input_string):
        return len(input_string) 
    
    def to_uppercase(self, input_string):
        return input_string.upper()
    
obj_string_manipulator = StringManipulator()
char_val=obj_string_manipulator.find_character("Testing",'e')
print(f"Index of a char is :: {char_val}")
length_of_val=obj_string_manipulator.find_length("Testing")
upper_case_value=obj_string_manipulator.to_uppercase("testing")
print(f"Length of a string is :: {length_of_val}")
print(f"Uppercase value of a string is ::",upper_case_value)