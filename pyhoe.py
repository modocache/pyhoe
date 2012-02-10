import sys
import types
import argparse
from pyhoe import commands as cmds
from pyhoe.commands import *

COMMANDS = list((
    cmds.__dict__.get(c) for c in dir(cmds) if isinstance(
        cmds.__dict__.get(c), types.ModuleType
    )
))

def available_command_names():
    """
    Returns a list of command names in pyhoe.commands.
    """
    return [c.__name__.split(".")[-1] for c in COMMANDS]


if __name__ == "__main__":
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
        choices = available_command_names(),
        help = "Choose an action for pyhoe to perform."
    )
    parser.add_argument(
        "options",
        nargs = "*",
        help = (
            "Add any option flags or positional arguments for "
            "the specified action. You can see options by simply "
            "entering the action name."
        )
    )

    # Print help if no args provided.
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(0) # TODO - Perhaps exit with error?

    # Pass remaining args to appropriate function.
    args = vars(parser.parse_args(sys.argv[1:]))
    for c in COMMANDS:
        if args["action"] == c.__name__.split(".")[-1]:
            c.execute(sys.argv[2:])
