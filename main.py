import random
from hangman_words import word_list
from hangman_art import stages, logo

#The clear() function can only be used on replit.com
from replit import clear

print(logo)
chosen_word = random.choice(word_list)
end_game = True
lives = 6

display = []
for n in range(0, len(chosen_word)):
  display += "_"

while end_game:
  guess = input("Guess a letter: ").lower()

  clear()

  if guess in display:
    print("You've already guessed that letter.")

  for n in range(0, len(chosen_word)):
    letter = chosen_word[n]
    if letter == guess:
      display[n] = letter
  each_letter = ' '.join(display)
  print(each_letter)
 
  if guess not in display:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_game = False
      print(f"The word is: {chosen_word}. You lose.")

  if "_" not in display:
    end_game = False
    print("You win.")
    
  print(stages[lives])
