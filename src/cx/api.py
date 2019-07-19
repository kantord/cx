from flask import Flask
from flask_restful import Resource, Api
from cx.rates import get_arbitrary_rate
from cx.dates import parse_date

app = Flask(__name__)
api = Api(app)

db = {}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Rate(Resource):
    def get(self, date, from_, to):
        return {"rate": get_arbitrary_rate(db, parse_date(date), from_, to)}


api.add_resource(HelloWorld, '/')
api.add_resource(Rate, '/rate/<string:date>/<string:from_>/<string:to>')

if __name__ == '__main__':
    app.run(debug=True)
