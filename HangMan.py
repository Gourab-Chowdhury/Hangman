import random
import hangman_art
#import hangman_words

from hangman_words import word_list
chosen_word = random.choice(word_list)  #Randomly choose a word from the word_list and assign it to a variable called chosen_word.

length = len(chosen_word)  #For each letter in the chosen_word, add a "_" to 'display'.

lives = 6  #a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.

#from hangman_art import logo
print (hangman_art.logo)

#Create blanks
display=[]  #Create an empty List called display.
for _ in range(length): #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each etter to guess.
  display += "_"

end_of_game = False

while not end_of_game:
   
  guess = input("Guess a letter: ").lower()   #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  
  #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  for position in range(length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter 
  #print (display) #Print 'display' and see the guessed letter in the correct position and every other letter replace with "_".

 #If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
 #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You Loss.")
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(hangman_art.stages[lives])