Colorize
==========

Give some color to your (remote) TTY!!

Usage
----------

Currently there are two way to use it:

### Rendering the output ###

	:::
		$ command to execute | colorize.py

If you need to render both the stdout and the stderr:

	:::
		$ command to execute |& colorize.py

This method works well with too long outputs

### As runner ###

	:::
		$ colorize.py command to execute

This method can do disgusting things with too long outputs.


Configuration File
----------

It will find a configuration file in the current directory, in the home directory or in the default path directory. The first one found will be used. So, it will search for:

- *./.colorize.conf*
- *$HOME/.configuration/colorize/colorize.conf*
- */etc/colorize/colorize.conf*

The format for this file is very easy: it is a CSV file with next fields:

-----------------------------------------------------------------------------------------------------------
|          | regular expression to highlight (quoted) | bold output | foreground color | background color |
-----------------------------------------------------------------------------------------------------------
| Example: | "^=+$"                                   | 1           | white            |                  |
| Example: | "^=+$"                                   | true        | white            | black            |
| Example: | "^=+$"                                   | 0           | red              | white            |
| Example: | "^=+$"                                   | false       | brown            | magenta          |
-----------------------------------------------------------------------------------------------------------

Available colors:

- *black*
- *white*
- *red*
- *green*
- *blue*
- *brown*
- *gray*
- *magenta*
- *cyan*

And that's all.

Example to simulate colordiff
----------

	:::
		"^>.*", 0, blue
		"^<.*", 0, red
		"^\d+,?\d*c\d+,?\d*$", 0, magenta

That's enough :D
