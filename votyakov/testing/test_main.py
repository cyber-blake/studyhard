# content of test_tmp_path.py
import pytest


def test_needsfiles(tmp_path):
    print(tmp_path)
    assert False


a = 1


def test_vua():
    assert a % 2 == 0, "value was odd, should be even"


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass


import sys


@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_function():
    assert True
