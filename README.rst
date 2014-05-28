Colorize
========

Give some color to your (remote) TTY!!

==============  ===============  =========  ============
VERSION         DOWNLOADS        TESTS      COVERAGE
==============  ===============  =========  ============
|pip version|   |pip downloads|  |travis|   |coveralls|
==============  ===============  =========  ============

And it is free. Checkout the `Source code`_.


Installation and Usage
----------------------

Two options: to install it in your system/project::

    pip install colorize

And you can use it with::

    python -m colorize -h


Or just `download the lastest zip`_ and use it with::

   python colorize-X.Y.Z.zip -h


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

.. Uso:


.. |travis| image:: https://travis-ci.org/magmax/colorize.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/colorize/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://pypip.in/v/colorize/badge.png
    :target: `project`_
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/colorize/badge.png
    :target: `project`_
    :alt: Number of PyPI downloads

.. _Travis: https://travis-ci.org/magmax/colorize
.. _Coveralls: https://coveralls.io/r/magmax/colorize
.. _project: https://pypi.python.org/pypi/colorize
.. _download the lastest zip: https://pypi.python.org/pypi/colorize
.. _Source code: https://github.com/magmax/colorize
