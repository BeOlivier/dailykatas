from dailykatas import (
    do_i_get_a_bonus, 
    count_the_monkeys
)

def test_monkey_count():
    assert count_the_monkeys.monkey_count(5) == [i for i in range(1, 6)]
    
def test_do_i_get_a_bonus():
    assert do_i_get_a_bonus.bonus_time(2, True) == '$20'
    assert do_i_get_a_bonus.bonus_time(5, True) == '$50'
    assert do_i_get_a_bonus.bonus_time(10, True) == '$100'
    assert do_i_get_a_bonus.bonus_time(10, False) == '$10'