"""Codewars kata solutions, ordered from hardest to easiest."""

import math
import string

# ---------------------------------------------------------------------------
# 5 kyu
# ---------------------------------------------------------------------------

# Human Readable Time
def make_readable(seconds):
    return f"{seconds//3600 :02d}:{(seconds%3600)//60 :02d}:{(seconds%60) :02d}"

# Simple Pig Latin
def pig_it(text):
    words = text.split()
    result = []
    punctuation = "!#€%&/=?"

    for word in words:
        if word[0] not in punctuation:
            result.append(f"{word[1:]}{word[0]}ay")
        else:
            result.append(word)

    return " ".join(result)

# ---------------------------------------------------------------------------
# 6 kyu
# ---------------------------------------------------------------------------

import re

# Convert string to camel case
def to_camel_case(text):
    words = re.split(r"[-_]", text)
    return words[0] + "".join(word.title() for word in words[1:])

# Persistent Bugger
def persistence(num):
    list_digits = [int(i) for i in str(num)]
    steps = 0
    
    while len(list_digits) > 1:
        temp = 1
        for i in list_digits:
            temp *= i
        list_digits = [int(i) for i in str(temp)]
        steps += 1
    return steps

# Replace With Alphabet Position
def alphabet_position(text):
    result = []

    for char in text.lower():
        if char.isalpha():
            result.append(str(ord(char) - ord("a") + 1))
    return " ".join(result)

# Duplicate Encoder
def duplicate_encode(word):
    word = word.lower()
    result_str = ""
    for i in word:
        if word.count(i) == 1:
            result_str += "("
        else:
            result_str += ")"
    return result_str

# Count the number of Duplicates
def duplicate_count(text):
    text = text.lower()
    list_result = []
    for i in text:
        if (text.count(i) > 1 and i not in list_result):
            list_result.append(i)
    return len(list_result)

# Find the Parity Outlier
def find_outlier(numbers):
    odd = []
    even = []
    for number in numbers:
        if number%2 == 0:
            even.append(number)
        else:
            odd.append(number)
    if len(even) == 1:
        return even[0]
    return odd[0]

# Count bits
def countBits(n):
    return bin(n).count("1")

# Create Phone Number
def create_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)


# ---------------------------------------------------------------------------
# 7 kyu
# ---------------------------------------------------------------------------

# Highest and Lowest
def high_and_low(numbers):
    values = list(map(int, numbers.split()))
    return f"{max(values)} {min(values)}"


# Square Every Digit
def square_digits(number):
    return int("".join(str(int(digit) ** 2) for digit in str(number)))


# Vowel Count
def get_count(text):
    return sum(character in "aeiou" for character in text)


# Disemvowel Trolls
def disemvowel(text):
    return text.translate({ord(vowel): None for vowel in "aeiouAEIOU"})


# ---------------------------------------------------------------------------
# 8 kyu
# ---------------------------------------------------------------------------

# Calculate Age
def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    if age == 0:
        return "You were born this very year!"
    if age == 1:
        return "You are 1 year old."
    if age > 1:
        return f"You are {age} years old."
    if age == -1:
        return "You will be born in 1 year."
    return f"You will be born in {-age} years."


# Regex Count Lowercase Letters
def lowercase_count(text):
    return sum(character in string.ascii_lowercase for character in text)


# Grasshopper - Check for Factor
def check_for_factor(base, factor):
    return base % factor == 0


# Twice as Old
def twice_as_old(father_age, son_age):
    return abs(father_age - 2 * son_age)


# Keep Up the Hoop
def hoop_count(number):
    if number < 10:
        return "Keep at it until you get it"
    return "Great, now move on to tricks"


# Beginner Series #4 Cockroach
def cockroach_speed(speed):
    return math.floor(speed * 100000 / 3600)


# Will There Be Enough Space?
def enough(capacity, on_bus, waiting):
    return max(0, on_bus + waiting - capacity)


# L1: Set Alarm
def set_alarm(employed, vacation):
    return employed and not vacation


# Removing Elements
def remove_every_other(items):
    return items[::2]


# Remove Every Third Element
def remove_every_third(items):
    return items[::3]


# Third Angle of a Triangle
def other_angle(first_angle, second_angle):
    return 180 - first_angle - second_angle


# Do I Get a Bonus?
def bonus_time(salary, bonus):
    return f"${salary * 10 if bonus else salary}"


# Count the Monkeys!
def monkey_count(number):
    return list(range(1, number + 1))
