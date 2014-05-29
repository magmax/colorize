from __future__ import unicode_literals
import unittest
import pexpect


class stdin_is_colorized_test(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn('python -m colorize', timeout=3)

    def test_normal_output(self):
        self.sut.sendline('example')

        self.sut.expect_exact('example', timeout=3)

    def test_case_is_important(self):
        self.sut.sendline('failure')

        self.sut.expect_exact('failure', timeout=3)

    def test_failure_is_highlighted(self):
        self.sut.sendline('FAILURE')

        self.sut.expect_exact('\x1b[1;37;41mFAILURE\x1b[m',
                              timeout=3)
