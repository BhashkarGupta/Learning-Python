# Selection of a word from a list
import random
word_bank = ["ELEPHANT", "CAMEL", "DONKEY", "PEACOCK", "DRAGON", "WATER", "BISCUIT", "TIGER", "SMARTPHONE", "COMPUTER", "KEYBOARD", "COUNTRYSIDE", "SCHOOL", "COLLEGE", "INDIA"]
chosen_word = word_bank[random.randint(0, len(word_bank) - 1)]

# Generating blank word for user
blank_word = []
for x in chosen_word:
    blank_word.append("_")
print(chosen_word)

# adding ascii image as list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

game_image = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''']

# Printing logo
print("Welcome to the game called")
print(logo)
# Asking for user Input and comparing with chosen word
error_count = 0
guess_letter = input("Please Guess a letter - ").upper()
count_position = 0
match_count = 0
print_blank_word = ""
for y in chosen_word:
    count_position += 1
    if y == guess_letter:
        blank_word[count_position-1] = y
    else:
        match_count += 1
old_error_count = error_count
if match_count == len(chosen_word):
    error_count += 1
for w in blank_word:
    print_blank_word += w
print(game_image[error_count])
if error_count != old_error_count:
    print("Wrong Guess, Please try again.")
print(print_blank_word)

# Looping till we get the no of error to hang the man
while error_count <= 5 and print_blank_word != chosen_word:
    guess_letter = input("Please Guess another letter - ").upper()
    count_position = 0
    match_count = 0
    print_blank_word = ""
    for y in chosen_word:
        count_position += 1
        if y == guess_letter:
            blank_word[count_position-1] = y
        else:
            match_count += 1
    old_error_count = error_count
    if match_count == len(chosen_word):
        error_count += 1
    for w in blank_word:
        print_blank_word += w
    print(game_image[error_count])
    if guess_letter.upper() in blank_word:
        print("You have already guessed this letter.")
    if error_count != old_error_count:
        print("Wrong Guess, You loose a life. \nPlease try again.")
    print(print_blank_word)

# printing the result
if print_blank_word == chosen_word:
    print("\nThank you so much! :-), \nYou have saved the Man from being hang.")
elif error_count == 6:
    print("Sorry! \nYou have failed to save an innocent man from being hung. :-( ")


