import main

def test_problem():
    assert main.get_problem() == 3

def test_is_prime_3():
    assert main.is_prime(3) == True

def test_is_prime_5():
    assert main.is_prime(5) == True

def test_is_prime_7():
    assert main.is_prime(7) == True

def test_get_factors_6():
    assert main.get_factors(6) == [2,3]
