#Week3- Activity 2: count the words in the demo text file
#Develop a new project that reads demo.txt and returns the total number of words. 
#Share the GitHub repository link and a screenshot of the result.
 
class FileReader:
  
    def word_counter(self, file_path):
        with open(file_path,"r") as file:
         number_of_words = file.read().split(" ")
         file.close()
         return len(number_of_words)


if __name__ == "__main__":
 file_path = "Week-3-Assignment/demo.txt"
 file_reader = FileReader()
 print(f"No of words in a file are :: {file_reader.word_counter(file_path)}")