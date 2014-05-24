#!/usr/bin/python

# Copyright (C) 2012 Miguel Angel Garcia <miguelangel.garcia@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import re
import csv
import subprocess
from threading import Thread

APP_NAME = 'colorize'
APP_DESC = 'Colorizes the output of any command'
APP_VERSION = '0.0.0.3'


class Color(object):
    COLOR = '\033[{}m'
    NORMAL = COLOR.format('')
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

        properties.append(self.__getBoldString())
        if self.foreground:
            properties.append(self.__getForegroundString())
        if self.background:
            properties.append(self.__getBackgroundString())

        return self.COLOR.format(';'.join(properties))

    def __getBoldString(self):
        if self.bold:
            return '1'
        return '0'

    def __getForegroundString(self):
        return '3' + self.colors[self.foreground]

    def __getBackgroundString(self):
        return '4' + self.colors[self.background]


class Configuration(object):
    def __init__(self):
        self.regexp = {}

    def process(self):
        for filename in [self.configfile_currentdir(),
                         self.configfile_home(),
                         self.configfile_default()]:
            if os.path.exists(filename):
                self.__parse_config(filename)
                break

    def configfile_currentdir(self):
        return '.{}.conf'.format(APP_NAME)

    def configfile_home(self):
        return os.path.expanduser('~/.config/{0}/{0}.conf'.format(APP_NAME))

    def configfile_default(self):
        return '/etc/{0}/{0}.conf'.format(APP_NAME)

    def __parse_config(self, filename):
        with open(filename) as fd:
            reader = csv.reader(fd)
            for row in reader:
                if not row or (row[0] and row[0][0] == '#'):
                    continue

                row += 4*[None]

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
            print(self.replace(line.rstrip()))

    def replace(self, line):
        result = line
        for exp, color in self.regexps.items():
            result, _ = re.subn(exp, color, result)
        return result

    def flush(self):
        Thread.join(self, 1)


class Colorize(object):
    def __init__(self, config):
        self.regexp = config.regexp
        self.regexps = {}
        self.return_code = 0

    def run(self):
        self.compile_regexps()

        if len(sys.argv) == 1:
            colorizer = PrinterThread(sys.stdin, self.regexps)
            colorizer.flush()
        else:
            process = subprocess.Popen(sys.argv[1:],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            outpid = PrinterThread(process.stdout, self.regexps)
            errpid = PrinterThread(process.stderr, self.regexps)
            process.wait()
            outpid.flush()
            errpid.flush()
            self.return_code = process.returncode

    def compile_regexps(self):
        for exp, color in self.regexp.items():
            regexp = '({})'.format(exp)
            compiled = re.compile(regexp)
            self.regexps[compiled] = '{}\\1{}'.format(color, Color.NORMAL)

    def replace(self, line):
        result = line
        for exp, color in self.regexps.items():
            result, _ = re.subn(exp, color, result)
        return result


def main():
    conf = Configuration()
    conf.process()
    colorize = Colorize(conf)
    colorize.run()
    sys.exit(colorize.return_code)

if __name__ == '__main__':
    main()
