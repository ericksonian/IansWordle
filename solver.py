
def check_guess(word):
    output = ""
    for i, letter in enumerate(word):
        if letter == target_word[i]:
            output += letter
        else:
            output += "-"
    return output


def update_correct_pos(checked, so_far):
    if not correct_pos:
        so_far = '-' * len(target_word)

    so_far_list = list(so_far)

    for i, letter in enumerate(checked):
        if letter == target_word[i]:
            so_far_list[i] = letter
        else:
            so_far_list[i] = so_far_list[i]
    return ''.join(so_far_list)



def print_output(word, test):
    global masked_word
    masked_word = target_word
    output = ""
    for i, letter in enumerate(word):
        if letter.lower() == test[i]:  # Check for correct position
            output += "\033[92m{}\033[0m".format(letter.upper())  # set color to green
            # Update masked word to remove correct letter
            masked_word = masked_word[:i] + '-' + masked_word[i+1:]
        elif letter.lower() in masked_word and masked_word.index(letter.lower()) != i:  # Check for incorrect position in adjusted masked word
            if masked_word[i] == '-':
                output += "\033[92m{}\033[0m".format(letter.upper())  # correct letter already guessed
            else:
                output += "\033[93m{}\033[0m".format(letter.upper())  # set color to yellow
                print(masked_word)
        else:
            output += "\033[30m{}\033[0m".format(letter.upper())  # set color to black
    return output