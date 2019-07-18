from cx.exceptions import UnknownCurrencyError

VALID_CURRENCIES = {"EUR", "USD", "CZK", "PLN"}
BASE_CURRENCY = "EUR"
assert BASE_CURRENCY in VALID_CURRENCIES


def get_base_rate(db, date, to):
    "Currency conversion the base currency and another currency on a given date"


def get_arbitrary_rate(db, date, from_, to):
    "Currency conversion between any two currencies on a given date"

    if from_ not in VALID_CURRENCIES:
        raise UnknownCurrencyError('Currency "{}" is unknown'.format(from_))
    if to not in VALID_CURRENCIES:
        raise UnknownCurrencyError('Currency "{}" is unknown'.format(to))
    if from_ == to:
        return 1.0

    if from_ == BASE_CURRENCY:
        return get_base_rate(db=db, date=date, to=to)

    if to == BASE_CURRENCY:
        return 1 / get_base_rate(db=db, date=date, to=from_)

    return get_base_rate(db=db, date=date, to=to) / get_base_rate(db=db, date=date, to=from_)
