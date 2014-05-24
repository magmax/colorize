#!/usr/bin/python

from freshen import *
from freshen.checks import *
import os
import shlex
import subprocess
import StringIO
from colorize import colorize


# BEFORE
@Before
def before(sc):
    scc.tmp_dir = []
    scc.tmp_file = []
    scc.cwd = os.getcwd()
    scc.stdout = None
    scc.stderr = None
    scc.status = None


# AFTER
@After
def after(sc):
    for path in scc.tmp_file:
        os.remove(path)

    for path in reversed(scc.tmp_dir):
        os.rmdir(path)


# GIVEN
@Given('the directory "([\w/]+)"')
def create_directory(path):
    current = ''
    for each in path.split('/'):
        current += each

        if not os.path.exists(current):
            os.mkdir(current)
            scc.tmp_dir.append(current)
        current += os.path.sep


@Given('a file named "([A-z0-9_/.-]+)" that contains "(.*)"')
def create_file(path, content):
    with open(path, 'w+') as fd:
        if content:
            for line in content.split('\\n'):
                fd.write(line)
                fd.write('\n')
        scc.tmp_file.append(path)


@Given('a file named "([A-z0-9_/.-]+)"$')
def create_empty_file(path):
    create_file(path, '')


# WHEN
@When('I use as stdin "(.+)"$')
def run_stdin(input_stream):
    command = ['./colorize/colorize.py']
    process = subprocess.Popen(command,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    process.stdin.write(input_stream)
    scc.stdout, scc.stderr = process.communicate()
    scc.status = process.returncode


@When('I run colorize (.*)')
def run_colorize(args):
    args_list = shlex.split(args)
    command = ['./colorize/colorize.py'] + args_list
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    scc.stdout, scc.stderr = process.communicate()
    scc.status = process.returncode


# THEN
@Then('it should (pass|fail)')
def check_status(exp_status):
    if exp_status == "fail":
        assert_not_equals(scc.status, 0)
    elif scc.status != 0:
        print scc.exception
        raise Exception("Failed with exit status %d\nOUTPUT:\n%s"
                        % (scc.status, scc.stdout))


@Then('it should return (\d+)$')
def check_status_given(rc):
    assert_equals(scc.status, int(rc))


@Then('output is "(.*)"$')
def check_output0(exp_output):
    assert_equals(normalize(exp_output), scc.stdout.strip())


@Then('output contains "(.+)"$')
def check_output1(exp_output):
    assert_true(exp_output in scc.stdout,
                'Text "{0}", was not found in "{1}"'
                .format(exp_output, scc.stdout))


@Then('output not contains "(.+)"$')
def check_output2(exp_output):
    assert_false(exp_output in scc.stdout,
                 'Text "{0}", was found in "{1}"'
                 .format(exp_output, scc.stdout))


def normalize(string):
    return string.rstrip().replace('\\x1b', '\x1b')
