import sys
import colorize


def main():
    conf = colorize.Configuration()
    conf.process()
    c = colorize.Colorize(conf)
    c.run()
    sys.exit(c.return_code)


if __name__ == '__main__':
    main()
