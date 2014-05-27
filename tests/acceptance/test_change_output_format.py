from __future__ import unicode_literals
import unittest
import pexpect


class format_the_output(unittest.TestCase):
    def test_basic_format(self):
        self.sut = pexpect.spawnu(
            "python -m colorize -f 'a%(message)sa' -- echo FAILURE",
            timeout=1)

        self.sut.expect_exact('a\x1b[1;37;41mFAILURE\x1b[ma')
        self.assertEquals(0, self.sut.wait())

    def test_just_stdout(self):
        self.sut = pexpect.spawnu(
            "python -m colorize -f 'a%(message)sa' -- echo FAILURE",
            timeout=1)

        self.sut.expect_exact('a\x1b[1;37;41mFAILURE\x1b[ma')
        self.assertEquals(0, self.sut.wait())
