import datetime
import pytest
from cx.common.database import Database
from cx.common.exceptions import MissingDataError


def test_db_get_value(fs):
    fs.create_file('./price.db', contents="P 2017-08-05 EUR 2 USD")
    my_db = Database()
    assert my_db.get(datetime.date(2017, 8, 5)) == {
        "USD": 2
    }


def test_reads_updates_from_files(fs):
    fs.create_file('/price.db', contents="P 2017-08-05 EUR 2 USD\n")
    my_db = Database()
    with open('./price.db', "w") as fp:
        fp.write("P 2018-08-05 EUR 2 USD\n")
    my_db.last_update = datetime.date(2010, 8, 5)
    assert my_db.get(datetime.date(2018, 8, 5)) == {
        "USD": 2
    }


def test_avoid_unnecessary_updates(fs):
    fs.create_file('./price.db', contents="P 2017-08-05 EUR 2 USD\n")
    my_db = Database()
    with open('./price.db', "w") as fp:
        fp.write("P 2018-08-05 EUR 2 USD\n")
    with pytest.raises(MissingDataError):
        my_db.get(datetime.date(2018, 8, 5))


@pytest.mark.parametrize('date_string,date', (("2018-04-03", datetime.date(2018, 4, 3)), ("2017-03-01", datetime.date(2017, 3, 1))))
def test_single_date_missing_data(fs, date_string, date):
    fs.create_file('./price.db', contents="P 2017-08-05 EUR 2 USD\n")
    fake_db = Database()
    fake_db.data = {}
    with pytest.raises(MissingDataError, match="No data for date {}".format(date_string)):
        fake_db.get(date)
