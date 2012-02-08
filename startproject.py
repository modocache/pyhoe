#!/usr/bin/env python

import argparse
from cmdline import CommandLineDelegator

def parse_cl_args():
    """
    Uses argparse to handle user input.
    Returns a __dict__ representation of
    the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description = (
            "Initializes a Python project using established best practices."
        )
    )
    parser.add_argument(
        "project_name",
        help = "The name of the project."
    )
    parser.add_argument(
        "-p", "--python",
        dest = "python_exe",
        help = (
            "The Python interpreter to use, e.g.: "
            "--python=python2.6 will use the Python "
            "2.6 interpreter to create any new virtual "
            "environments."
        ),
    )
    parser.add_argument(
        "-y", "--yes-to-all",
        action = "store_true",
        help = (
            "Skip all confirmation and use recommended settings."
        )
    )
    return vars(parser.parse_args())

if __name__ == "__main__":
    delegator = CommandLineDelegator(parse_cl_args())
    delegator.execute()
