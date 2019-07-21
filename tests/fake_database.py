from cx.common.database import Database


class FakeDatabase(Database):
    def __init__(self, fake_data):
        self.data = fake_data

    def update(self):
        pass
