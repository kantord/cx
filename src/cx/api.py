from flask import Flask
from flask_restful import Resource, Api
from cx.rates import get_arbitrary_rate
from cx.dates import parse_date
from cx.pricedb import parse_line, build_db

app = Flask(__name__)
api = Api(app)

with open('./price.db') as input_file:
    db = build_db(map(parse_line, input_file))

class Rate(Resource):
    def get(self, date, from_, to):
        return {"rate": get_arbitrary_rate(db, parse_date(date), from_, to)}


api.add_resource(Rate, '/rate/<string:date>/<string:from_>/<string:to>')

if __name__ == '__main__':
    app.run(debug=True)
