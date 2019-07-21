from cx.common.dates import parse_date
from cx.common.currency import BASE_CURRENCY
from cx.common.exceptions import MissingDataError
from cx.common.dates import DATE_FORMAT
from cx.common.currency import validate_currency


def get_base_rate(db, date, to):
    "Currency conversion the base currency and another currency on a given date"
    validate_currency(to)

    if to not in db.get(date):
        raise MissingDataError("No data for currency \"{}\" on date {}".format(
            to, date.strftime(DATE_FORMAT)))

    return db.get(date)[to]


def get_arbitrary_rate(db, date, from_, to):
    "Currency conversion between any two currencies on a given date"

    validate_currency(from_)
    validate_currency(to)

    if from_ == to:
        return 1.0

    if from_ == BASE_CURRENCY:
        return get_base_rate(db=db, date=date, to=to)

    if to == BASE_CURRENCY:
        return 1 / get_base_rate(db=db, date=date, to=from_)

    return get_base_rate(db=db, date=date, to=to) / get_base_rate(db=db, date=date, to=from_)
