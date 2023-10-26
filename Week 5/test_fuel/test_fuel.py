# Roger Hennessy
# 10-10-2023

import pytest
import fuel

# Create our tests
def test_convert():
    # Test_convert() expects a str - if x > y == valueerror - if y == 0 ZeroDivisionError
    assert fuel.convert("1/2") == 50
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/100") == 1

def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"

def test_value_error():
    with pytest.raises(ValueError):
        fuel.convert("2/1")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

