from cx.common.pricedb import parse_line, build_db


class Database():
    def __init__(self):
        self.update()

    def update(self):
        with open('./price.db') as input_file:
            self.data = build_db(map(parse_line, input_file))

    def get(self, key):
        return self.data.get(key)


db = Database()
