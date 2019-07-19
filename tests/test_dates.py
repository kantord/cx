import pytest
import datetime
from cx.dates import parse_date
from cx.exceptions import InvalidDateError


@pytest.mark.parametrize('message,input_', (('"asd" is not a valid date', "asd"), ('"42" is not a valid date', 42)))
def test_parse_date_incorrect_date(message, input_):
    with pytest.raises(InvalidDateError, match=message):
        parse_date(input_)


@pytest.mark.parametrize('date,input_', ((datetime.date(2017, 5, 3), "2017-5-3"), (datetime.date(2018, 8, 2), "2018-08-02")))
def test_parse_date_correct_date(date, input_):
    assert parse_date(input_) == date
