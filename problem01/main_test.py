import main

def test_problem():
    assert main.get_problem() == 1


def test_sum_10_is_23():
    assert main.get_sum_from_max(10) == 23