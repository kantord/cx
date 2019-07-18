# -*- coding: utf-8 -*-

import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from datetime import date
from cx.logic import get_arbitrary_rate
from cx.logic import validate_currency
from cx.exceptions import UnknownCurrencyError


def test_validate_currency():
    validate_currency("EUR")
    validate_currency("USD")

    with pytest.raises(UnknownCurrencyError, match='Currency "geci" is unknown'):
        validate_currency("geci")

    with pytest.raises(UnknownCurrencyError, match='Currency "kurva" is unknown'):
        validate_currency("kurva")


def test_get_arbitrary_rate_validate_source_currency():
    db = {}
    source_currency = MagicMock()

    validate_currency_ = MagicMock()
    with patch('cx.logic.validate_currency', new=validate_currency_):
        try:
            get_arbitrary_rate(db=db, date=date(
                2018, 5, 11), from_=source_currency, to="EUR")
        except:
            pass

    validate_currency_.assert_any_call(source_currency)


def test_get_arbitrary_rate_validate_target_currency():
    db = {}
    target_currency = MagicMock()

    validate_currency_ = MagicMock()
    with patch('cx.logic.validate_currency', new=validate_currency_):
        try:
            get_arbitrary_rate(db=db, date=date(
                2018, 5, 11), to=target_currency, from_="EUR")
        except:
            pass

    validate_currency_.assert_any_call(target_currency)


def test_get_arbitrary_rate_identical_currencies():
    db = {}
    assert get_arbitrary_rate(db=db, date=date(
        2018, 5, 11), from_="USD", to="USD") == 1.0


def test_get_arbitrary_rate_converting_from_base_currency_correct_call():
    db = {}
    get_base_rate = MagicMock()
    with patch('cx.logic.get_base_rate', new=get_base_rate):
        get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="EUR", to="USD")
    get_base_rate.assert_called_with(db=db, date=date(2018, 5, 11), to="USD")


def test_get_arbitrary_rate_converting_to_base_currency_correct_call():
    db = {}
    get_base_rate = MagicMock()
    with patch('cx.logic.get_base_rate', new=get_base_rate):
        get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="USD", to="EUR")
    get_base_rate.assert_called_with(db=db, date=date(2018, 5, 11), to="USD")


def test_get_arbitrary_rate_converting_from_base_currency_correct_value():
    db = {}
    get_base_rate = MagicMock()
    get_base_rate.return_value = MagicMock()
    with patch('cx.logic.get_base_rate', new=get_base_rate):
        assert get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="EUR", to="USD") == get_base_rate.return_value


def test_get_arbitrary_rate_converting_to_base_currency_correct_value():
    db = {}
    get_base_rate = MagicMock()
    get_base_rate.return_value = 5
    with patch('cx.logic.get_base_rate', new=get_base_rate):
        assert get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="USD", to="EUR") == pytest.approx(1 / get_base_rate.return_value)


def test_get_arbitrary_rate_converting_arbitrary_currency_correct_call():
    db = {}
    get_base_rate = MagicMock()
    with patch('cx.logic.get_base_rate', new=get_base_rate):
        get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="CZK", to="USD")
    get_base_rate.assert_any_call(db=db, date=date(2018, 5, 11), to="USD")
    get_base_rate.assert_any_call(db=db, date=date(2018, 5, 11), to="CZK")


@pytest.mark.parametrize('currency,rate', (("CZK", 5), ("PLN", 3.5)))
def test_get_arbitrary_rate_converting_arbitrary_currency_correct_value(currency, rate):
    db = {}
    get_base_rate = MagicMock()
    get_base_rate.side_effect = lambda db, date, to: rate if to == currency else 2
    with patch('cx.logic.get_base_rate', new=get_base_rate):
        assert get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="USD", to=currency) == pytest.approx(rate / 2)
