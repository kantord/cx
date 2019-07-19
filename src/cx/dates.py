
import datetime
from cx.exceptions import InvalidDateError


DATE_FORMAT = "%Y-%m-%d"


def parse_date(date_string):
    try:
        return datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    except:
        raise InvalidDateError('"{}" is not a valid date'.format(date_string))
