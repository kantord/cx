from flask_restful import Resource
from cx.db import db
from cx.common.rates import get_arbitrary_rate
from cx.common.dates import parse_date
from cx.common.currency import BASE_CURRENCY


class SingleRate(Resource):
    def get(self, date, from_, to):
        return {"rate": get_arbitrary_rate(db, parse_date(date), from_, to)}


class Day(Resource):
    def get(self, date):
        return {"base": BASE_CURRENCY, "rates": db.get(parse_date(date))}
