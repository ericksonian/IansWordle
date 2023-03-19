
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

