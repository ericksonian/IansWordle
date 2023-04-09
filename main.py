import random


# Read in the list of valid words
with open("valid_words.txt", "r") as f:
    valid_words = [word.strip() for word in f]

# Read in the list of basic words
with open("en_basic.txt", "r") as f:
    words = [word.strip() for word in f]
# Filter the list to only include 5-letter words and lowercase
words = [word.lower() for word in words if len(word) == 5]

# Set Target Word
target_word = random.choice(words)
# target_word = 'stall'
masked_word = target_word

guess = ""
correct_pos = []
correct_pos_str = ""
num_guesses = 0
max_guesses = 6


def is_english(word):
    # Reading file line by line to save memory, instead of as a single string
    #    return word in valid_words.read().split()
    # Opening the file in the function so that it always starts at the beginning
    with open("valid_words.txt", "r") as wordle_words:
        for line in wordle_words:
            if line.strip() == word:
                return True
    return False


def is_valid(word):
    while len(word) != 5:
        print("5 Letters Required")
        word = input()
    result = is_english(word)
    while not result:
        print("Invalid Guess")
        word = input()
        result = is_english(word)
    return word


def print_output(word, test):
    global masked_word
    masked_word = target_word
    output = ""
    print(masked_word)
    for i, letter in enumerate(word):
        if letter.lower() == test[i]:  # Check for correct position
            # Update masked word to remove correct letter
            masked_word = masked_word[:i] + '-' + masked_word[i+1:]
        elif letter.lower() != test[i]:
            masked_word = masked_word
    print(masked_word)
    for i, letter in enumerate(word):
        if masked_word[i] == '-':
            output += "\033[92m{}\033[0m".format(letter.upper())                # correct letter already guessed
            print(masked_word + " G")
        elif letter.lower() in masked_word:
            output += "\033[93m{}\033[0m".format(letter.upper())    # set color to yellow
            index = masked_word.index(letter.lower())
            masked_word = masked_word[:index] + '*' + masked_word[index + 1:]   # remove Yellow letter from Masked Word
            print(masked_word + " Y")
        else:
            output += "\033[30m{}\033[0m".format(letter.upper())  # set color to black
    return output


print("Ian's Wordle")
print("Guess a Word:")

while target_word != guess:
    guess = is_valid(input("").lower())
    print("       " + print_output(guess, target_word))
    if target_word != guess:
        num_guesses += 1
        if num_guesses >= max_guesses:
            print("The word was: " + target_word)
            break
    else:
        print("You took " + str(num_guesses + 1) + " guesses")
