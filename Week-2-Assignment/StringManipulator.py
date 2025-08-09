class StringManipulator:
    def __init__(self, text):
        self.text = text
        
    def find_character(self, char):
        return self.text.find(char)
    
    def find_length(self):
        return len(self.text) 
    
    def to_uppercase(self):
        return self.text.upper()
    
obj_string_manipulator = StringManipulator("test")
char_val=obj_string_manipulator.find_character('e')
print(f"Index of a char is :: {char_val}")
length_of_val=obj_string_manipulator.find_length()
upper_case_value=obj_string_manipulator.to_uppercase()
print(f"Length of a string is :: {length_of_val}")
print(f"Uppercase value of a string is ::",upper_case_value)