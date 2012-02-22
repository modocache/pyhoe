#!/usr/bin/env python

import sys
import argparse


COMMANDS = ("sow",)


def import_child(module_name):
    """Dynamically imports child of specified module."""
    module = __import__(module_name)
    for layer in module_name.split('.')[1:]:
        module = getattr(module, layer)
    return module


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
    args = vars(parser.parse_args(sys.argv[1:2]))
    for c in COMMANDS:
        if args["action"] == c:
            # FIXME - pyhoe shouldn't be hard-coded here.
            import_child("pyhoe.%s.command" % c).execute(sys.argv[2:])


if __name__ == "__main__":
    main()
