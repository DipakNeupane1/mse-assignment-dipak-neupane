#Week 2 - Activity 5: Develop a project to work with Strings
#Develop a project using class and methods to get a sentence from user input and find the number of words in it.

class WordSeparator:
    
    def seperate_word_from_sentence(self, sentence):
        split_into_words = sentence.split()
        print(f"After spliting given sentence into words is :: {split_into_words}")
        return len(split_into_words)
    
word_seperator = WordSeparator();
number_of_words = word_seperator.seperate_word_from_sentence("Hello, this is calls of psd week-2 assignment")
print(f"Numbers of words in given sentence is :: {number_of_words}")