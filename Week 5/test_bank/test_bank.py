# Roger Hennessy
# 07-10-2023

import bank

# Create our test()
def test_greeting():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hey") == 20
    assert bank.value("HEY") == 20
    assert bank.value("something") == 100
    assert bank.value("SOMETHING") == 100
