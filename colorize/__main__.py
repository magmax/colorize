import sys
from .colorize import Configuration
from .colorize import Colorize


def main():
    conf = Configuration()
    conf.process()
    colorize = Colorize(conf)
    colorize.run()
    sys.exit(colorize.return_code)


if __name__ == '__main__':
    main()
