import random
import hangman_art
import hangman_words

stages = hangman_art.stages
end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
lives = 6

print(hangman_art.logo)
print("\n")

print(chosen_word)

#Create blanks
display = []
for _ in chosen_word:
  display.append("_")

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  if guess in display:
    print(f"You already guessed '{guess}' in this game.")
    
  for index, letter in enumerate(chosen_word):
    if letter == guess:
      display[index] = letter

  if guess not in chosen_word:
    lives -= 1
    print(f"Letter '{guess}' is not in the word")
    if lives == 0:
      end_of_game = True
      print("You loose!")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win!")

  print(stages[lives])
