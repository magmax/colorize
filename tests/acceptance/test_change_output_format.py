from __future__ import unicode_literals
import time
import unittest
import pexpect


class format_the_output(unittest.TestCase):
    def test_basic_format(self):
        self.sut = pexpect.spawnu(
            "python -m colorize -f 'a%(message)sa' -- echo FAILURE",
            timeout=3)

        self.sut.expect_exact('a\x1b[1;37;41mFAILURE\x1b[ma')
        self.assertEquals(0, self.sut.wait())

    def test_just_stdout(self):
        self.sut = pexpect.spawnu(
            "python -m colorize -f 'b%(message)sb' -- echo FAILURE",
            timeout=3)

        self.sut.expect_exact('b\x1b[1;37;41mFAILURE\x1b[mb')
        self.assertEquals(0, self.sut.wait())

    def test_normal_output(self):
        self.sut = pexpect.spawnu(
            "python -m colorize -f 'b%(message)sb' -- echo foo",
            timeout=3)

        self.sut.expect_exact('bfoob')
        self.assertEquals(0, self.sut.wait())

    def test_format_date(self):
        format = '%Y-%m-%d'
        self.sut = pexpect.spawnu(
            "python -m colorize -f '%(asctime)s'"
            " --date-format='{f}'"
            " -- echo foo".format(f=format),
            timeout=3)

        output = self.sut.read()
        parsed = time.strptime(output.strip(), format)
        self.assertEquals(time.strftime(format),
                          time.strftime(format, parsed))
