
all::

tests::
	./colorize/colorize.py nosetests -s -v --with-freshen tests

testsbn::
	nosetests -s -v --with-freshen tests

package::
