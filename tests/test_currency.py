# -*- coding: utf-8 -*-

import pytest
from cx.logic import validate_currency
from cx.exceptions import UnknownCurrencyError


def test_validate_currency():
    validate_currency("EUR")
    validate_currency("USD")

    with pytest.raises(UnknownCurrencyError, match='Currency "geci" is unknown'):
        validate_currency("geci")

    with pytest.raises(UnknownCurrencyError, match='Currency "kurva" is unknown'):
        validate_currency("kurva")
