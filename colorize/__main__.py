import sys
import argparse
import logging

from .colorize import Configuration
from .colorize import Colorize
from . import __description__


def logging_setup(args):
    logging.basicConfig(
        level=logging.INFO,
        format=args.format,
        datefmt='%m-%d %H:%M:%S',)


def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('command', nargs='*',
                        help='Command to be executed')
    parser.add_argument('-f', '--format', default='%(message)s',
                        help='Configures both stdout and stderr')
    parser.add_argument('--format-out', default='%(message)s',
                        help='Configures the output format')

    args = parser.parse_args()

    logging_setup(args)

    conf = Configuration()
    conf.process()
    colorize = Colorize(conf)
    colorize.process_command(args.command)
    sys.exit(colorize.return_code)


if __name__ == '__main__':
    main()
