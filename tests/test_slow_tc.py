import sys

import pytest
from Apps.Calculator import add

@pytest.mark.slow
def test_add():
    assert add(3,6)==9

@pytest.mark.skip(reason="Not implemeted yet")
def test_subtract():
    return False

@pytest.mark.skipif(sys.platform=="win32",reason="Addition failed")
def test_expectedtoskip_withreason():
    return False

@pytest.mark.xfail
def test_expectedtofail():
    return True