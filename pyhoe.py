import sys, os
import argparse
import pyhoe

try:
    import sneaze
    SNEAZR_ENABLED = True
except ImportError:
    SNEAZR_ENABLED = False

# Each command is represented by a directory.
# Inelegant but suits our purposes for the time being.
MAIN_DIRECTORY = "pyhoe"
COMMANDS = [
    d for d in os.listdir(MAIN_DIRECTORY) if os.path.isdir(
        os.path.join(MAIN_DIRECTORY, d)
    )
]

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
        choices = COMMANDS,
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
        if args["action"] == c:
            module = "pyhoe.%s.command" % c
            __import__(module).execute(sys.argv[2:])
