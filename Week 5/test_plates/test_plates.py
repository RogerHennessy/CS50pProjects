# Roger Hennessy
# 08-10-2023

import plates

# Do some tests
def test_first_two_letters():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("50") == False

def test_length():
    assert plates.is_valid("qw") == True
    assert plates.is_valid("qwr5455") == False

def test_puncuation():
    assert plates.is_valid("qw405") == True
    assert plates.is_valid("qw4-5") == False

def test_number():
    assert plates.is_valid("qw405") == True
    assert plates.is_valid("qw4a5") == False
    assert plates.is_valid("qw045") == False
