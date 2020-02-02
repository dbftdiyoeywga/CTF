def cipher(strings, n_shift=3):
    new_strings = ""
    upper_range = [ord('A'), ord('Z')]
    lower_range = [ord('a'), ord('z')]

    for c in strings:
        if (upper_range[0] <= ord(c) <= upper_range[1]):
            new_strings += chr((ord(c) - ord("A") + n_shift) % 26 + ord("A"))
        elif (lower_range[0] <= ord(c) <= lower_range[1]):
            new_strings += chr((ord(c) - ord("a") + n_shift) % 26 + ord("a"))
        else:
            new_strings += c

    return new_strings


strings = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"

print(cipher(strings, -3))