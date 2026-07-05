# Welcome!
# These are all the 8 kyu katas from codewars that I have solved so far.
# Each function has the name of the kata above it in a comment as they are called on codewars.

# modules for various functions
import math
import string

def calculate_age(y, c):
    if y < c:
        if c-y == 1:
            return f"You are 1 year old."
        return f"You are {c-y} years old."
    if y > c:
        if y-c == 1:
            return f"You will be born in {y-c} year."
        return f"You will be born in {y-c} years."
    else:
        return "You were born this very year!"

def lowercase_count(str):
    alphabet_lc = string.ascii_lowercase
    count = 0
    for i in str:
        if i in alphabet_lc:
            count += 1
    return count

# Grasshopeer - check for factor
def check_for_factor(base, factor):
    return base % factor == 0

# Twice as old
def twice_as_old(d, s):
    return abs(d - 2*s)

# Keep up the hoop
def hoop_count(n):
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"

# Beginner Series #4 Cockroach
def cockroach_speed(s):
    return math.floor(s*100000/3600)

# Will there be enough space?
enough = lambda cap, on, wait : 0 if cap >= on + wait else -(cap - on - wait)

# L1: Set Alarm
def set_alarm(employed, vacation):
    return employed and not vacation

# Removing elements
def remove_every_other(my_list):
    return my_list[::2]

def remove_every_third(my_list):
    return my_list[::3]

# Third angle of a triangle
other_angle = lambda a, b : 180 - a - b

# Do I get a bonus?
bonus_time = lambda salary, bonus : "$"+ str(salary) if bonus == False else "$" + str(salary * 10)