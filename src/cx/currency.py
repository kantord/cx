from cx.exceptions import UnknownCurrencyError

VALID_CURRENCIES = {"EUR", "USD", "CZK", "PLN"}
BASE_CURRENCY = "EUR"
assert BASE_CURRENCY in VALID_CURRENCIES


def validate_currency(currency):
    "Verifies the validity of a currency"

    if currency not in VALID_CURRENCIES:
        raise UnknownCurrencyError('Currency "{}" is unknown'.format(currency))
