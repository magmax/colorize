#!/usr/bin/python

import os
import sys
import re
import csv
import thread
import subprocess
from threading import Thread

APP_NAME = 'colorize'
APP_DESC = 'Colorizes the output of any command'
APP_VERSION = '0.0.0.3'

class Color(object):
    NORMAL = '\033[m'
    COLOR = '\033[{}m'
    colors = {
	'black':       '0',
	'red':         '1',
	'green':       '2',
	'brown':       '3',
	'blue':        '4',
	'magenta':     '5',
	'cyan':        '6',
	'white':       '7',
        }

    def __init__(self, bold=False, foreground=None, background=None):
        self.bold = bold
        self.foreground = foreground
        self.background = background

    def __str__(self):
        properties = []
        if self.bold:
            properties.append('1')
        else:
            properties.append('0')

        if self.foreground:
            properties.append('3' + self.colors[self.foreground])
        if self.background:
            properties.append('4' + self.colors[self.background])

        return self.COLOR.format(';'.join(properties))


class Configuration(object):
    def __init__(self):
        self.regexp = {}

    def process(self):
        for filename in [self.configfile_currentdir(), self.configfile_home(), self.configfile_default()]:
            if os.path.exists(filename):
                self.__parse_config(filename)
                break;

    def configfile_currentdir(self):
        return '.{}.conf'.format(APP_NAME)

    def configfile_home(self):
        return os.path.expanduser('~/.config/{0}/{0}.conf'.format(APP_NAME))

    def configfile_default(self):
        return '/etc/{0}/{0}.conf'.format(APP_NAME)

    def __parse_config(self, filename):
        with file(filename) as fd:
            reader = csv.reader(fd)
            for row in reader:
                if not row or (row[0] and row[0][0] == '#'):
                    continue

                row += 5*[None]

                regexp = row[0]
                color = Color()
                if row[1]:
                    color.bold = row[1].strip().lower() in ['1', 'true']
                if row[2]:
                    color.foreground = row[2].strip()
                if row[3]:
                    color.background = row[3].strip()

                self.regexp[regexp] = color

class PrinterThread(Thread):
    def __init__(self, fdin, regexps):
        super(PrinterThread, self).__init__()
        self.fdin = fdin
        self.regexps = regexps
        self.start()

    def run(self):
        while not self.fdin.closed:
            line = self.fdin.readline()
            if line == '':
                break
            print self.replace(line.rstrip())

    def replace(self, line):
        result = line
        for exp, color in self.regexps.items():
            result = re.subn(exp, color, result )[0]
        return result

    def flush(self):
        Thread.join(self, 1)


class Colorize(object):
    def __init__(self, config):
        self.regexp = config.regexp
        self.regexps = {}

    def run(self):
        self.compile_regexps()

        if len(sys.argv) == 1:
            colorizer = PrinterThread(sys.stdin, self.regexps)
            colorizer.flush()
        else:
            process = subprocess.Popen(sys.argv[1:], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outpid = PrinterThread(process.stdout, self.regexps)
            errpid = PrinterThread(process.stderr, self.regexps)
            process.wait()
            outpid.flush()
            errpid.flush()
            return

    def compile_regexps(self):
        for exp, color in self.regexp.items():
            regexp = '(' + exp + ')'
            compiled = re.compile(regexp)
            self.regexps[compiled] = str(color) + '\\1' + Color.NORMAL

    def replace(self, line):
        result = line
        for exp, color in self.regexps.items():
            result = re.subn(exp, color, result )[0]
        return result

def main():
    conf = Configuration()
    conf.process()
    colorize = Colorize(conf)
    colorize.run()

if __name__ == '__main__':
    main()
