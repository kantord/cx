# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for cx.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest


@pytest.fixture
def api(fs):
    fs.create_file('./price.db', contents="")
    from cx.api import app
    return app.test_client()
