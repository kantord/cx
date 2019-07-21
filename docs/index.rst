==
cx
==

This is the documentation of **cx** currency exchange API.


Setup & Run
-----------

.. code:: bash

        sudo docker build . -t cx
        sudo docker run -p 5000:5000 cx:latest


Resources
---------

Rates
^^^^^

This resource contains information about the exchanges rates on a certain day between two currencies.

.. note::
        As exchange rates are not published on weekends and bank holidays, there is no data available for such dates

To fetch an exchange rate you have to make a GET request to the ``/rates`` endpoint. Example:

.. code:: bash

        curl http://127.0.0.1:5000/rates/2018-05-23/PLN/EUR

will result in the following JSON reply:

.. code:: json

        { "rate": 0.23208317861121427 }

If you want to get all exchange rates on a single day you can omit the source and target currency from the same GET request:

.. code:: bash

        curl http://127.0.0.1:5000/rates/2018-05-23

you can except a response like this:

.. code:: json

        {
            "base": "EUR",
            "rates": {
                "USD": 1.1708,
                "CZK": 25.813,
                "PLN": 4.3088
            }
        }




Contents
========

.. toctree::
   :maxdepth: 2

   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _toctree: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: http://www.sphinx-doc.org/en/stable/markup/inline.html
.. _Python domain syntax: http://sphinx-doc.org/domains.html#the-python-domain
.. _Sphinx: http://www.sphinx-doc.org/
.. _Python: http://docs.python.org/
.. _Numpy: http://docs.scipy.org/doc/numpy
.. _SciPy: http://docs.scipy.org/doc/scipy/reference/
.. _matplotlib: https://matplotlib.org/contents.html#
.. _Pandas: http://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: http://scikit-learn.org/stable
.. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _Google style: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists
