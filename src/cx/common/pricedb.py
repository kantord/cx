"""
Utility functions for parsing ledger-cli pricedb files
"""

import datetime
from collections import defaultdict
from cx.common.dates import parse_date
from cx.common.currency import validate_currency
from cx.common.exceptions import UnknownCurrencyError


def parse_line(input_):
    "Parse a line from a ledger-cli pricedb file"
    parts = input_.split('\n')[0].split(' ')
    raw_date = parts[1]
    raw_rate = parts[3]
    currency = parts[4]
    date = parse_date(raw_date)
    rate = float(raw_rate)

    return (date, rate, currency)


def build_db(lines):
    "Build a price database from parsed lines"
    results = defaultdict(dict)

    for line in lines:
        date, rate, currency = line
        try:
            validate_currency(currency)
            results[date].update({currency: rate})
        except UnknownCurrencyError:
            pass

    return dict(results)
