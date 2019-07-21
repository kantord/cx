from flask import Flask
from flask_restful import Api
from cx.resources import rates

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)


api.add_resource(rates.SingleRate,
                 '/rates/<string:date>/<string:from_>/<string:to>')
api.add_resource(rates.Day, '/rates/<string:date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
