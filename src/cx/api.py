from flask import Flask
from flask_restful import Resource, Api
from cx.rates import get_arbitrary_rate
from cx.dates import parse_date
from cx.currency import BASE_CURRENCY
from cx.pricedb import parse_line, build_db

app = Flask(__name__)
api = Api(app)

with open('./price.db') as input_file:
    db = build_db(map(parse_line, input_file))


class SingleRate(Resource):
    def get(self, date, from_, to):
        return {"rate": get_arbitrary_rate(db, parse_date(date), from_, to)}


class Day(Resource):
    def get(self, date):
        return {"base": BASE_CURRENCY, "rates": db[parse_date(date)]}


api.add_resource(SingleRate, '/rates/<string:date>/<string:from_>/<string:to>')
api.add_resource(Day, '/rates/<string:date>')

if __name__ == '__main__':
    app.run(debug=True)
