import datetime
from cx.db import Database


def test_db_get_value(fs):
    # "fs" is the reference to the fake file system
    fs.create_file('./price.db', contents="P 2017-08-05 EUR 2 USD")
    my_db = Database()
    assert my_db.get(datetime.date(2017, 8, 5)) == {
        "USD": 2
    }
