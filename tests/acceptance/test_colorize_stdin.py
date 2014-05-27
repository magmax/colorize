from __future__ import unicode_literals
import unittest
import pexpect


class stdin_is_colorized_test(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn('python -m colorize', timeout=1)

    def test_normal_output(self):
        self.sut.sendline('example')
        self.sut.sendeof()

        self.sut.expect_exact('example')
        self.assertEquals(0, self.sut.wait())

    def test_case_is_important(self):
        self.sut.sendline('failure')
        self.sut.sendeof()

        self.sut.expect_exact('failure')
        self.assertEquals(0, self.sut.wait())

    def test_failure_is_highlighted(self):
        self.sut.sendline('FAILURE')
        self.sut.sendeof()

        self.sut.expect_exact('\x1b[1;37;41mFAILURE\x1b[m')
        self.assertEquals(0, self.sut.wait())
