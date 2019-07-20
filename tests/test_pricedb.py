import pytest
import datetime
from cx.pricedb import parse_line, build_db

examples = (
    ("P 2019-07-18 EUR 1.1216 USD", datetime.date(2019, 7, 18), 1.1216, "USD"),
    ("P 2016-04-08 EUR 120.89 JPY", datetime.date(2016, 4, 8), 120.89, "JPY"),
    ("P 2019-07-18 EUR 1.9558 BGN", datetime.date(2019, 7, 18), 1.9558, "BGN"),
    ("P 2017-11-08 EUR 25.586 CZK", datetime.date(2017, 11, 8), 25.586, "CZK"),
    ("P 2017-11-08 EUR 25.586 CZK\n", datetime.date(2017, 11, 8), 25.586, "CZK"),
)


@pytest.mark.parametrize('input_,date,rate,currency', examples)
def test_parse_line(input_, date, rate, currency):
    assert parse_line(input_) == (date, rate, currency)


def test_build_db_empty_input():
    assert build_db([]) == dict()


def test_build_db_single_input():
    assert build_db([examples[0][1:]]) == {
        datetime.date(2019, 7, 18): {"USD": 1.1216}}


def test_build_db_same_date():
    assert build_db([examples[0][1:], examples[2][1:]]) == {
        datetime.date(2019, 7, 18): {"USD": 1.1216, "BGN": 1.9558}}


def test_build_db_different_date():
    assert build_db([examples[0][1:], examples[1][1:]]) == {
        datetime.date(2019, 7, 18): {"USD": 1.1216},
        datetime.date(2016, 4, 8): {"JPY": 120.89}
    }
