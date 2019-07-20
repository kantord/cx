import pytest
import datetime
from unittest.mock import patch
from cx.currency import BASE_CURRENCY


@pytest.mark.parametrize('date_string,from_,to,value', (("2018-04-03", "USD", "CZK", 1), ("2017-03-01", "CZK", "USD", 2)))
def test_rates_single_return_value(api, date_string, from_, to, value):
    fake_db = {
        datetime.date(2018, 4, 3): {
            "USD": 2,
            "CZK": 2,
        },
        datetime.date(2017, 3, 1): {
            "USD": 4,
            "CZK": 2,
        },
    }

    with patch('cx.api.db', new=fake_db):
        result = api.get('rates/{}/{}/{}'.format(date_string, from_, to))
    assert result.json == {"rate": value}


@pytest.mark.parametrize('date_string,value', (("2018-04-03", {
    "USD": 2,
    "CZK": 2,
}), ("2017-03-01", {
    "USD": 4,
    "CZK": 2,
})))
def test_rates_singe_date_return_value(api, date_string, value):
    fake_db = {
        datetime.date(2018, 4, 3): {
            "USD": 2,
            "CZK": 2,
        },
        datetime.date(2017, 3, 1): {
            "USD": 4,
            "CZK": 2,
        },
    }

    with patch('cx.api.db', new=fake_db):
        result = api.get('rates/{}'.format(date_string))
    assert result.json == {
        "base": BASE_CURRENCY,
        "rates": value
    }
