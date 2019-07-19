# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for cx.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest

from cx.api import app


@pytest.fixture
def api():
    return app.test_client()
