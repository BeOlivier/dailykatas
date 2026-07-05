import katas


# ---------------------------------------------------------------------------
# 5 kyu
# ---------------------------------------------------------------------------

def test_make_readable():
    assert katas.make_readable(0) == "00:00:00"
    assert katas.make_readable(59) == "00:00:59"
    assert katas.make_readable(60) == "00:01:00"
    assert katas.make_readable(3599) == "00:59:59"
    assert katas.make_readable(3600) == "01:00:00"
    assert katas.make_readable(86399) == "23:59:59"
    assert katas.make_readable(86400) == "24:00:00"
    assert katas.make_readable(359999) == "99:59:59"


def test_pig_it():
    assert katas.pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert katas.pig_it("This is my string") == "hisTay siay ymay tringsay"
    assert katas.pig_it("Hello world !") == "elloHay orldway !"
    assert katas.pig_it("Quis custodiet ipsos custodes ?") == "uisQay ustodietcay psosiay ustodescay ?"
    assert katas.pig_it("Python") == "ythonPay"


# ---------------------------------------------------------------------------
# 6 kyu
# ---------------------------------------------------------------------------

def test_alphabet_position():
    assert katas.alphabet_position("The sunset sets at twelve o' clock.") == (
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    )
    assert katas.alphabet_position("The narwhal bacons at midnight.") == (
        "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
    )


def test_duplicate_encode():
    assert katas.duplicate_encode("din") == "((("
    assert katas.duplicate_encode("recede") == "()()()"
    assert katas.duplicate_encode("Success") == ")())())"
    assert katas.duplicate_encode("(( @") == "))(("


def test_duplicate_count():
    assert katas.duplicate_count("") == 0
    assert katas.duplicate_count("abcde") == 0
    assert katas.duplicate_count("abcdeaa") == 1
    assert katas.duplicate_count("abcdeaB") == 2
    assert katas.duplicate_count("Indivisibilities") == 2


def test_find_outlier():
    assert katas.find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert katas.find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
    assert katas.find_outlier([2, 6, 8, -10, 3]) == 3
    assert katas.find_outlier([-1, -3, -5, -2, -7]) == -2


def test_count_bits():
    assert katas.countBits(0) == 0
    assert katas.countBits(4) == 1
    assert katas.countBits(7) == 3
    assert katas.countBits(9) == 2
    assert katas.countBits(10) == 2


def test_create_phone_number():
    assert katas.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert katas.create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == "(012) 345-6789"


# ---------------------------------------------------------------------------
# 7 kyu
# ---------------------------------------------------------------------------

def test_high_and_low():
    assert katas.high_and_low("1 2 3 4 5") == "5 1"
    assert katas.high_and_low("1 2 -3 4 5") == "5 -3"
    assert katas.high_and_low("1 9 3 4 -5") == "9 -5"
    assert katas.high_and_low("42") == "42 42"


def test_square_digits():
    assert katas.square_digits(9119) == 811181
    assert katas.square_digits(1234) == 14916


def test_get_count():
    assert katas.get_count("aeiou") == 5
    assert katas.get_count("This is a test") == 4


def test_disemvowel():
    assert katas.disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"


# ---------------------------------------------------------------------------
# 8 kyu
# ---------------------------------------------------------------------------

def test_calculate_age():
    assert katas.calculate_age(1990, 2024) == "You are 34 years old."
    assert katas.calculate_age(2023, 2024) == "You are 1 year old."
    assert katas.calculate_age(2024, 2024) == "You were born this very year!"
    assert katas.calculate_age(2025, 2024) == "You will be born in 1 year."
    assert katas.calculate_age(2030, 2024) == "You will be born in 6 years."


def test_lowercase_count():
    assert katas.lowercase_count("abcABC123!") == 3
    assert katas.lowercase_count("") == 0
    assert katas.lowercase_count("HELLO") == 0
    assert katas.lowercase_count("a!b.c?d e") == 5
    assert katas.lowercase_count("abcdefghijklmnopqrstuvwxyz") == 26
    assert katas.lowercase_count("Hello World") == 8


def test_check_for_factor():
    assert katas.check_for_factor(10, 2) is True
    assert katas.check_for_factor(63, 7) is True
    assert katas.check_for_factor(9, 2) is False
    assert katas.check_for_factor(24612, 13) is False


def test_twice_as_old():
    assert katas.twice_as_old(36, 7) == 22
    assert katas.twice_as_old(55, 30) == 5
    assert katas.twice_as_old(42, 21) == 0


def test_hoop_count():
    assert katas.hoop_count(3) == "Keep at it until you get it"
    assert katas.hoop_count(11) == "Great, now move on to tricks"


def test_cockroach_speed():
    assert katas.cockroach_speed(1.08) == 30
    assert katas.cockroach_speed(0) == 0
    assert katas.cockroach_speed(1.09) == 30


def test_enough():
    assert katas.enough(10, 5, 5) == 0
    assert katas.enough(100, 60, 50) == 10
    assert katas.enough(100, 100, 100) == 100
    assert katas.enough(33, 17, 45) == 29


def test_set_alarm():
    assert katas.set_alarm(True, True) is False
    assert katas.set_alarm(False, True) is False
    assert katas.set_alarm(True, False) is True
    assert katas.set_alarm(False, False) is False


def test_other_angle():
    assert katas.other_angle(30, 60) == 90
    assert katas.other_angle(10, 20) == 150


def test_bonus_time():
    assert katas.bonus_time(2, True) == "$20"
    assert katas.bonus_time(5, True) == "$50"
    assert katas.bonus_time(10, False) == "$10"


def test_remove_every_other():
    assert katas.remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]) == ["Keep", "Keep", "Keep"]
    assert katas.remove_every_other([1, 2, 3, 4, 5, 6]) == [1, 3, 5]


def test_remove_every_third():
    assert katas.remove_every_third([1, 2, 3, 4, 5, 6]) == [1, 4]
    assert katas.remove_every_third(["a", "b", "c", "d", "e", "f"]) == ["a", "d"]


def test_monkey_count():
    assert katas.monkey_count(5) == [1, 2, 3, 4, 5]
    assert katas.monkey_count(1) == [1]
