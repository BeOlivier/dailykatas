from dailykatas.katas import (
    do_i_get_a_bonus,
    removing_elements
)



    
def test_do_i_get_a_bonus():
    assert do_i_get_a_bonus.bonus_time(2, True) == '$20'
    assert do_i_get_a_bonus.bonus_time(5, True) == '$50'
    assert do_i_get_a_bonus.bonus_time(10, True) == '$100'
    assert do_i_get_a_bonus.bonus_time(10, False) == '$10'
    
def test_remove_every_other():
    assert removing_elements.remove_every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert removing_elements.remove_every_other(['a', 'b', 'c', 'd', 'e']) == ['a', 'c', 'e']
    assert removing_elements.remove_every_other([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert removing_elements.remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]) == ["Keep", "Keep", "Keep"]

def test_remove_every_third():
    assert removing_elements.remove_every_third([1, 2, 3, 4, 5, 6]) == [1, 4]
    assert removing_elements.remove_every_third(['a', 'b', 'c', 'd', 'e', 'f']) == ['a', 'd']    