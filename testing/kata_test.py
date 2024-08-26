from dailykatas.katas import (
    katas_8kyu,
    katas_7kyu
)

def test_hoop_count():
    assert katas_8kyu.hoop_count(3) == "Keep at it until you get it" 
    assert katas_8kyu.hoop_count(11) == "Great, now move on to tricks"

def test_disemvowel():
    assert katas_7kyu.disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"

def test_get_count():
    assert katas_7kyu.get_count("aeiou") == 5

def test_cockroach_speed():
    assert katas_8kyu.cockroach_speed(1.08) == 30
    assert katas_8kyu.cockroach_speed(0) == 0
    assert katas_8kyu.cockroach_speed(1.09) == 30

def test_enough():
    assert katas_8kyu.enough(10, 5, 5) == 0
    assert katas_8kyu.enough(100, 60, 50) == 10
    assert katas_8kyu.enough(100, 100, 100) == 100
    assert katas_8kyu.enough(100, 50, 50) == 0
    assert katas_8kyu.enough(33, 17, 45) == 29

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