import unittest
import doublex
from colorize import colorize

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


class PrinterTests(unittest.TestCase):
    def test_finished_for_closed_input(self):
        with doublex.Mock() as stdin:
            stdin.closed = True
        log = doublex.Stub()
        sut = colorize.Printer(stdin, {}, log)

        sut.process()

        doublex.assert_that(stdin, doublex.verify())

    def test_reads_a_line_and_prints_it(self):
        line = 'foo'
        stdin = StringIO(line.decode('utf-8'))
        with doublex.Mock() as log:
            log.log(line)

        sut = colorize.Printer(stdin, {}, log.log)

        sut.process()

        doublex.assert_that(log, doublex.verify())

    def test_reads_two_lines_and_prints_them(self):
        line = '1\n2'
        stdin = StringIO(line.decode('utf-8'))
        with doublex.Mock() as log:
            log.log('1')
            log.log('2')

        sut = colorize.Printer(stdin, {}, log.log)

        sut.process()

        doublex.assert_that(log, doublex.verify())

    def test_replacement(self):
        line = 'foo'
        stdin = StringIO(line.decode('utf-8'))
        expected = 'ok'
        with doublex.Mock() as log:
            log.log(expected)
        regexps = {'foo': expected}

        sut = colorize.Printer(stdin, regexps, log.log)

        sut.process()

        doublex.assert_that(log, doublex.verify())
