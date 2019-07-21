# -*- coding: utf-8 -*-

import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from datetime import date
from cx.common.rates import get_arbitrary_rate
from cx.common.rates import get_base_rate
from cx.common.exceptions import UnknownCurrencyError
from cx.common.exceptions import MissingDataError
from tests.fake_database import FakeDatabase


def test_get_base_rate_validate_currency(FakeDatabase):
    db = FakeDatabase(dict())
    fake_currency = MagicMock()

    validate_currency_ = MagicMock()
    with patch('cx.common.rates.validate_currency', new=validate_currency_):
        try:
            get_base_rate(db=db, date=date(
                2018, 5, 11), to=fake_currency)
        except:
            pass

    validate_currency_.assert_called_with(fake_currency)


@pytest.mark.parametrize('message,day', (("No data for date 2018-05-05", 5), ("No data for date 2018-05-03", 3)))
def test_get_base_rate_validate_date(message, day):
    with pytest.raises(MissingDataError, match=message):
        get_base_rate(db=FakeDatabase(dict()), date=date(
            2018, 5, day), to="CZK")


@pytest.mark.parametrize('message,currency', (('No data for currency "CZK" on date 2018-05-05', "CZK"), ('No data for currency "PLN" on date 2018-05-05', "PLN")))
def test_get_base_rate_validate_currency(message, currency):
    db = {
        date(2018, 5, 5): {}
    }
    with pytest.raises(MissingDataError, match=message):
        get_base_rate(FakeDatabase(db), date=date(2018, 5, 5), to=currency)


@pytest.mark.parametrize('date_,currency,value', ((date(2017, 5, 11), "CZK", 4), (date(2018, 5, 11), "PLN", 2)))
def test_get_base_rate_validate_currency(date_, currency, value):
    db = FakeDatabase({
        date(2017, 5, 11): {"CZK": 4},
        date(2018, 5, 11): {"PLN": 2},
    })
    assert get_base_rate(db, date=date_, to=currency) == value


def test_get_arbitrary_rate_validate_source_currency():
    db = FakeDatabase(dict())
    source_currency = MagicMock()

    validate_currency_ = MagicMock()
    with patch('cx.common.rates.validate_currency', new=validate_currency_):
        try:
            get_arbitrary_rate(db=db, date=date(
                2018, 5, 11), from_=source_currency, to="EUR")
        except:
            pass

    validate_currency_.assert_any_call(source_currency)


def test_get_arbitrary_rate_validate_target_currency():
    db = FakeDatabase(dict())
    target_currency = MagicMock()

    validate_currency_ = MagicMock()
    with patch('cx.common.rates.validate_currency', new=validate_currency_):
        try:
            get_arbitrary_rate(db=db, date=date(
                2018, 5, 11), to=target_currency, from_="EUR")
        except:
            pass

    validate_currency_.assert_any_call(target_currency)


def test_get_arbitrary_rate_identical_currencies():
    db = FakeDatabase(dict())
    assert get_arbitrary_rate(db=db, date=date(
        2018, 5, 11), from_="USD", to="USD") == 1.0


def test_get_arbitrary_rate_converting_from_base_currency_correct_call():
    db = FakeDatabase(dict())
    get_base_rate_ = MagicMock()
    with patch('cx.common.rates.get_base_rate', new=get_base_rate_):
        get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="EUR", to="USD")
    get_base_rate_.assert_called_with(db=db, date=date(2018, 5, 11), to="USD")


def test_get_arbitrary_rate_converting_to_base_currency_correct_call():
    db = FakeDatabase(dict())
    get_base_rate_ = MagicMock()
    with patch('cx.common.rates.get_base_rate', new=get_base_rate_):
        get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="USD", to="EUR")
    get_base_rate_.assert_called_with(db=db, date=date(2018, 5, 11), to="USD")


def test_get_arbitrary_rate_converting_from_base_currency_correct_value():
    db = FakeDatabase(dict())
    get_base_rate_ = MagicMock()
    get_base_rate_.return_value = MagicMock()
    with patch('cx.common.rates.get_base_rate', new=get_base_rate_):
        assert get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="EUR", to="USD") == get_base_rate_.return_value


def test_get_arbitrary_rate_converting_to_base_currency_correct_value():
    db = FakeDatabase(dict())
    get_base_rate_ = MagicMock()
    get_base_rate_.return_value = 5
    with patch('cx.common.rates.get_base_rate', new=get_base_rate_):
        assert get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="USD", to="EUR") == pytest.approx(1 / get_base_rate_.return_value)


def test_get_arbitrary_rate_converting_arbitrary_currency_correct_call():
    db = FakeDatabase(dict())
    get_base_rate_ = MagicMock()
    with patch('cx.common.rates.get_base_rate', new=get_base_rate_):
        get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="CZK", to="USD")
    get_base_rate_.assert_any_call(db=db, date=date(2018, 5, 11), to="USD")
    get_base_rate_.assert_any_call(db=db, date=date(2018, 5, 11), to="CZK")


@pytest.mark.parametrize('currency,rate', (("CZK", 5), ("PLN", 3.5)))
def test_get_arbitrary_rate_converting_arbitrary_currency_correct_value(currency, rate):
    db = FakeDatabase(dict())
    get_base_rate_ = MagicMock()
    get_base_rate_.side_effect = lambda db, date, to: rate if to == currency else 2
    with patch('cx.common.rates.get_base_rate', new=get_base_rate_):
        assert get_arbitrary_rate(db=db, date=date(
            2018, 5, 11), from_="USD", to=currency) == pytest.approx(rate / 2)
