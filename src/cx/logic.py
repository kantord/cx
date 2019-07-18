from cx.exceptions import UnknownCurrencyError

valid_currencies = {"EUR", "USD", "CZK", "PLN"}
base_currency = "EUR"
assert base_currency in valid_currencies

def get_base_rate(db, date, to):
    pass

def get_arbitrary_rate(db, date, from_, to):
    if from_ not in valid_currencies:
        raise UnknownCurrencyError('Currency "{}" is unknown'.format(from_))
    if to not in valid_currencies:
        raise UnknownCurrencyError('Currency "{}" is unknown'.format(to))
    if from_ == to:
        return 1.0

    if from_ == base_currency:
        return get_base_rate(db=db, date=date, to=to)

    if to == base_currency:
        return 1 / get_base_rate(db=db, date=date, to=from_)

    return get_base_rate(db=db, date=date, to=to) / get_base_rate(db=db, date=date, to=from_)
    

