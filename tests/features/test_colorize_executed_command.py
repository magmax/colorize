import unittest
import pexpect


class stdin_is_colorized_test(unittest.TestCase):
    def test_valid_output(self):
        self.sut = pexpect.spawn('python -m colorize echo FAILURE',
                                 timeout=1)

        self.sut.expect_exact('\x1b[1;37;41mFAILURE\x1b[m'.encode('utf-8'))
        self.assertEquals(0, self.sut.wait())

    def test_returns_2_if_child_returns_2(self):
        self.sut = pexpect.spawn('python -m colorize ls /foo',
                                 timeout=1)

        self.assertEquals(2, self.sut.wait())
