import datetime
from cx.common.pricedb import parse_line, build_db
from cx.common.dates import DATE_FORMAT
from cx.common.exceptions import MissingDataError


class Database():
    def __init__(self):
        self.last_update = None
        self.update()

    def needs_update(self):
        return not self.last_update or self.last_update < datetime.date.today()

    def update(self):
        if not self.needs_update():
            return

        with open('./price.db') as input_file:
            self.data = build_db(map(parse_line, input_file))
        self.last_update = datetime.date.today()

    def get(self, key):
        self.update()
        try:
            return self.data[key]
        except KeyError:
            raise MissingDataError(
                "No data for date {}".format(key.strftime(DATE_FORMAT)))
