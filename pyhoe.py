import sys
import argparse

# Each command is represented by a directory.
# Inelegant but suits our purposes for the time being.
PACKAGE_DIRECTORY = "pyhoe"
COMMANDS = ("startproject",)

def main():
    print "pyhoe.py:", sys.argv
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
        sys.exit(0) # TODO - Perhaps exit with error?

    # Pass remaining args to appropriate function.
    # FIXME - Hacky.
    args = vars(parser.parse_args(sys.argv[1:2]))
    for c in COMMANDS:
        if args["action"] == c:
            module = "%s.%s.command" % (PACKAGE_DIRECTORY, c)
            __import__(module, fromlist=["pyhoe"]).execute(sys.argv[2:])


if __name__ == "__main__":
    main()
