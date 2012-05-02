Colorize
==========

Give some color to your (remote) TTY!!

Usage
----------

Currently there is only one way to use it:

	:::
		$ command to execute | colorize.py


Configuration File
----------

It will find a configuration file in the current directory, in the home directory or in the default path directory. The first one found will be used.

The format for this file is very easy: it is a CSV file with next fields:

| regular expression to highlight (quoted) | bold output | foreground color | background color |

Available colors:
- black
- white
- red
- green
- blue
- brown
- gray
- magenta
- cyan

And that's all.

Example to simulate colordiff
----------

	:::
		"^>.*", 0, blue
		"^<.*", 0, red
		"^\d+,?\d*c\d+,?\d*$", 0, magenta

That's enough :D
