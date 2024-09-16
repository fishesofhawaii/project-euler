import main

def test_problem():
    assert main.get_problem() == 2

def test_invalid_fib_seed():
    assert main.get_next_fib([1]) == None

def test_valid_fib_seed():
    assert main.get_next_fib([1,2]) == 3

def test_valid_fib_seed_size_3():
    assert main.get_next_fib([1,2,3]) == 5

def test_does_meet_criteria_odd():
    assert main.does_meet_criteria(1) == False

def test_does_meet_criteria_even():
    assert main.does_meet_criteria(2) == True

def test_does_meet_criteria_4mill():
    assert main.does_meet_criteria(4000000) == False

def test_does_meet_criteria_3mill_even():
    assert main.does_meet_criteria(3000000) == True
