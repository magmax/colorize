Colorize
========

Give some color to your (remote) TTY!!

==============  ===============  =========  ============  =======
VERSION         DOWNLOADS        TESTS      COVERAGE      WHEEL
==============  ===============  =========  ============  =======
|pip version|   |pip downloads|  |travis|   |coveralls|   |wheel|
==============  ===============  =========  ============  =======

And it is free. Checkout the `Source code`_.


Installation and Usage
----------------------

Two options: to install it in your system/project::

    pip install colorize

And you can use it with::

    python -m colorize -h


Now, you have two ways to use it:

Rendering the output
~~~~~~~~~~~~~~~~~~~~

Just execute::

    $ command to execute | python -m colorize

If you need to render both the stdout and the stderr::

    $ command to execute |& python -m colorize

This method works well with too long outputs

As runner
~~~~~~~~~

Other way to use it:

    $ python -m colorize command to execute

This method can do disgusting things with too long outputs.

Options
-------

You can change the output format with the argument :code:`-f` or :code:`--format`. It uses the same format that ``logging``, so you can use any of its special variables, like:

- :code:`%(asctime)s`, to show the time.
- :code:`%(message)s`, to show the message itself.
- :code:`%(msecs)d`, to show the relative time.
- `Any other output format allowed by logging`_.

You can combine them as you wish. Example::

    $ python -m colorize -- echo foo
    foo
    $ python -m colorize -f "%(asctime)s - %(levelname).2s: %(message)s" -- echo foo
    05-29 08:43:09 - IN: foo
    $ python -m colorize -f "%(levelname).2s %(asctime)s - %(message)s" -- echo foo
    IN 05-29 08:44:17 - foo

Default date format is :code:`%m-%d %H:%M:%S`, but you can change it with :code:`--date-format`::

    $ python -m colorize -f "%(asctime)s" --date-format="%H:%M:%S" -- echo foo
    08:44:17
    $ python -m colorize -f "%(asctime)s" --date-format="%H %M %S" -- echo foo
    08 44 17


Configuration File
------------------

It will find a configuration file in the current directory, in the home directory or in the default path directory. The first one found will be used. So, it will search for:

- ``./.colorize.conf``
- ``$HOME/.configuration/colorize/colorize.conf``
- ``/etc/colorize/colorize.conf``

The format for this file is very easy: it is a CSV file with next fields::

    # regular expression to highlight (quoted) , bold output , foreground color , background color
      "^=+$"                                   , 1           , white            ,
      "^=+$"                                   , true        , white            , black
      "^=+$"                                   , 0           , red              , white
      "^=+$"                                   , false       , brown            , magenta

For example, you can configure it to colorize the `go test` output::

    "^PASS", 1, white, green
    "^ok", 1, white, green
    "^FAIL", 1, white, red
    "^--- FAIL:", 1, white, red


Available colors:

- :code:`black`
- :code:`white`
- :code:`red`
- :code:`green`
- :code:`blue`
- :code:`brown`
- :code:`gray`
- :code:`magenta`
- :code:`cyan`

And that's all.

Example to simulate colordiff
-----------------------------

To emulate colordiff, just use this configuration file::

    "^>.*",                0, blue
    "^<.*",                0, red
    "^\d+,?\d*c\d+,?\d*$", 0, magenta

That's enough :D


.. |travis| image:: https://travis-ci.org/magmax/colorize.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/colorize/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://img.shields.io/pypi/v/colorize.svg
    :target: `project`_
    :alt: Latest PyPI version

.. |pip downloads| image:: https://img.shields.io/pypi/dm/colorize.svg
    :target: `project`_
    :alt: Number of PyPI downloads

.. |wheel| image:: https://img.shields.io/pypi/wheel/colorize.svg
    :target: `project`_
    :alt: Wheel Status

.. _Travis: https://travis-ci.org/magmax/colorize
.. _Coveralls: https://coveralls.io/r/magmax/colorize
.. _project: https://pypi.python.org/pypi/colorize
.. _download the lastest egg: https://pypi.python.org/pypi/colorize#downloads
.. _Source code: https://github.com/magmax/colorize
.. _Any other output format allowed by logging: https://docs.python.org/3.5/library/logging.html#logrecord-attributes
