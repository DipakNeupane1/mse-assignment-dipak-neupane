import random
import string


class GuessTheWordGame:
 def generate_random_word(self):
    random_word = ''.join(random.choices(string.ascii_lowercase, k=8))
    return random_word

 def guess_the_word(self):
    number_of_lives = 10;
    random_word = set(self.generate_random_word())
    print(f"Random word is :: ", random_word)

    # Generate exact blanks in array as the letters in the random_word
    number_of_blanks_to_fill_from_guess = [" "] * len(random_word)
    
    word_matching_counter = 0;
    while(word_matching_counter!=len(random_word)):
      guessed_letter = input("Please enter a letter of your choice: ").lower()
      matched = False
      for i, letter in enumerate(random_word):
          if letter == guessed_letter:
              number_of_blanks_to_fill_from_guess[i] = guessed_letter
              word_matching_counter+=1
              matched= True
              print(f" Entered letter is matched :: ")
              if(word_matching_counter==len(random_word)):
                  print(f" Your guess is matched, and here is final array filled after guess:: ", number_of_blanks_to_fill_from_guess)
                  print(f" Your guess is matched, so game is over now, well done!!!")
                  return
      if(matched==False):
       print(f" Entered letter is not matched :: ")
       number_of_lives-=1
       print(f" Your remaining number of life is :: {number_of_lives}")
       if(number_of_lives<=0): 
           print(f" Your have crossed the lives limit, so game is over now!!!")
           return
    else: print(f" Your have crossed the lives limit, so game is over now!!!")
    return
            
# Create an instance of a class "GuessTheWordGame" and call the method/function inside it.
guess_the_word_game_obj= GuessTheWordGame()
guess_the_word_game_obj.guess_the_word()
