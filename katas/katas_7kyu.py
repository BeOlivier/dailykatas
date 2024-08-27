# Welcome!
# These are all the 7 kyu katas from codewars that I have solved so far.
# Each function has the name of the kata above it in a comment as they are called on codewars.

# modules for various functions

# Square Every Digit
def square_digits(num):
    string_num = str(num)
    result = ""
    for i in string_num:
        result += str(int(i)*int(i))
    print(result)
    return int(result)

# Vowel count
get_count = lambda s: sum(map(s.count, ['a', 'e', 'i', 'o', 'u']))

# Disemvowel Trolls
def disemvowel(s):
    return s.translate({ord(i): None for i in 'aeiouAEIOU'})