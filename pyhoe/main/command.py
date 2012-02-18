#!/usr/bin/env python

import sys
from os.path import dirname, join, abspath
import argparse

# FIXME - Imports don't seem to work unless I add package
# directories to my path. Surely this can't be the right
# way to do this.
PACKAGE_DIRECTORY = dirname(dirname(__file__))
sys.path.append(abspath(PACKAGE_DIRECTORY))
COMMANDS = ("sow",)
for cmd in COMMANDS:
    sys.path.append(join(PACKAGE_DIRECTORY, cmd))

def main():
    # Instantiate argument parser, add arguments.
    parser = argparse.ArgumentParser(
        prog="pyhoe",
        description = (
            "Provides several convenient functions for developing "
            "Python packages and scripts using best practices."
        )
    )
    parser.add_argument(
        "action",
        choices = COMMANDS,
        help = "Choose an action for pyhoe to perform."
    )
    parser.add_argument(
        "options",
        nargs = "*",
        default = argparse.SUPPRESS,
        help = (
            "Add any option flags or positional arguments for "
            "the specified action. You can see options by simply "
            "entering the action name."
        )
    )

    # Print help if no args provided.
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(0)

    # Pass remaining args to appropriate function.
    # FIXME - Hacky.
    args = vars(parser.parse_args(sys.argv[1:2]))
    for c in COMMANDS:
        if args["action"] == c:
            # FIXME - pyhoe shouldn't be hard-coded here.
            module = "pyhoe.%s.command" % (c)
            __import__(
                module, fromlist=[PACKAGE_DIRECTORY]
            ).execute(sys.argv[2:])


if __name__ == "__main__":
    main()
