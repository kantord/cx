# -*- coding: utf-8 -*-

import pytest
from cx.skeleton import fib

__author__ = "Dániel Kántor"
__copyright__ = "Dániel Kántor"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
