import random

# Read in the list of valid words
with open("valid_words.txt", "r") as f:
    valid_words = [word.strip() for word in f]

target_word = random.choice(valid_words)
guess = ""
correct_pos = []
correct_pos_str = ""
num_guesses = 0
max_guesses = 6


def is_english(word):
    # Reading File line by line to save memory, instead of as a single string
    #    return word in valid_words.read().split()
    # Opening the file in the function so that it always starts at the beginning
    with open("valid_words.txt", "r") as wordle_words:
        for line in wordle_words:
            if line.strip() == word:
                return True
    return False


def is_valid(word):
    while len(word) != 5:
        print("5 Letters ")
        word = input()
    result = is_english(word)
    while not result:
        print("Invalid ")
        word = input()
        result = is_english(word)
    return word


def print_output(word, test):
    output = ""
    for i, letter in enumerate(word):
        if letter.lower() == test[i]:
            output += "\033[92m{}\033[0m".format(letter.upper())  # set color to green
        elif letter.lower() in test:
            output += "\033[93m{}\033[0m".format(letter.upper())  # set color to yellow
        else:
            output += "\033[30m{}\033[0m".format(letter.upper())  # set color to black
    return output


# target_word = "plain"
# print(target_word)
print("Ian's Wordle")
print("Guess a Word:")

while target_word != guess:
    # print("Guess a Word:")
    guess = is_valid(input("").lower())
    #    print("Valid!")
    print("       " + print_output(guess, target_word))
    if target_word != guess:
        num_guesses += 1
        if num_guesses >= max_guesses:
            print("The word was: " + target_word)
            break
        # else:
            # print("You have " + str(max_guesses - num_guesses) + " guesses left")
    else:
        print("You took " + str(num_guesses + 1) + " guesses")
