import sys
import argparse

from .colorize import Configuration
from .colorize import Colorize
from . import __description__


def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('command', nargs='*',
                        help='Command to be executed')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    conf = Configuration()
    conf.process()
    colorize = Colorize(conf)
    colorize.process_command(args.command)
    sys.exit(colorize.return_code)


if __name__ == '__main__':
    main()
