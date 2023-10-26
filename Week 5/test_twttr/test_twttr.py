# Roger Hennessy
# 07-10-2023

import twttr

# Create our test()
def test_assert():
    assert twttr.shorten("test output") == "tst tpt"
    assert twttr.shorten("TEST OUTPUT") == "TST TPT"
    assert twttr.shorten("t3st 0utput") == "t3st 0tpt"
    assert twttr.shorten("!?t£$t 0^tp^t?!") == "!?t£$t 0^tp^t?!"