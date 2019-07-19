from cx.exceptions import MissingDataError
from cx.dates import DATE_FORMAT
from cx.currency import validate_currency, BASE_CURRENCY


def get_base_rate(db, date, to):
    "Currency conversion the base currency and another currency on a given date"
    validate_currency(to)

    if date not in db:
        raise MissingDataError(
            "No data for date {}".format(date.strftime(DATE_FORMAT)))

    if to not in db[date]:
        raise MissingDataError("No data for currency \"{}\" on date {}".format(
            to, date.strftime(DATE_FORMAT)))

    return db[date][to]


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
