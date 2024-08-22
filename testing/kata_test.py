from dailykatas.katas import katas_8kyu

def test_set_alarm():
    assert katas_8kyu.set_alarm(True, True) == False
    assert katas_8kyu.set_alarm(False, True) == False
    assert katas_8kyu.set_alarm(True, False) == True
    assert katas_8kyu.set_alarm(False, False) == False

def test_thirdofatriangle():
    assert katas_8kyu.other_angle(30, 60) == 90
    assert katas_8kyu.other_angle(10, 20) == 150
    
def test_do_i_get_a_bonus():
    assert katas_8kyu.bonus_time(2, True) == '$20'
    assert katas_8kyu.bonus_time(5, True) == '$50'
    assert katas_8kyu.bonus_time(10, False) == '$10'
    assert katas_8kyu.bonus_time(10, True) == '$100'
    
def test_remove_every_other():
    assert katas_8kyu.remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]) == ["Keep", "Keep", "Keep"]
    assert katas_8kyu.remove_every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert katas_8kyu.remove_every_other(['a', 'b', 'c', 'd', 'e']) == ['a', 'c', 'e']
    assert katas_8kyu.remove_every_other([1, 2, 3, 4, 5, 6]) == [1, 3, 5]

def test_remove_every_third():
    assert katas_8kyu.remove_every_third([1, 2, 3, 4, 5, 6]) == [1, 4]
    assert katas_8kyu.remove_every_third(['a', 'b', 'c', 'd', 'e', 'f']) == ['a', 'd']    