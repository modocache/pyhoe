#!/usr/bin/env python

import os, sys
import argparse
from pyhoe.delegator import BaseCommandDelegator

# FIXME - Place this somewhere 
TEMPLATE_DIR = "templates"

class StartProjectCommandDelegator(BaseCommandDelegator):
    pass


def default_temaplate():
    """
    Returns a string representing the default template directory.
    """
    default = "package"
    if default in os.listdir(TEMPLATE_DIR):
        return default
    else:
        return os.listdir(TEMPLATE_DIR)[0]


def parse(sysargs):
    """
    Uses argparse to handle user input.
    Returns a __dict__ representation of
    the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog="pyhoe startproject",
        description = (
            "Initializes a Python project using established best practices."
        )
    )
    parser.add_argument(
        "project_name",
        help = "The name of the project."
    )
    parser.add_argument(
        "-c", "--cucumber",
        action = "store_true",
        help = "Use freshen for behavior-driven development."
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
        "-t", "--template",
        choices = os.listdir(TEMPLATE_DIR),
        default = default_temaplate(),
        help = "The template to use for your project."
    )
    parser.add_argument(
        "-y", "--yes-to-all",
        action = "store_true",
        help = (
            "Skip all confirmation and use recommended settings."
        )
    )
    return vars(parser.parse_args(sysargs))


def execute(args=None):
    """
    Parses sys.args or args parameter and executes
    the parsed values using CommandLineDelegator.
    """
    a = args or sys.argv
    delegator = StartProjectCommandDelegator(parse(a))
    delegator.dispatch()


if __name__ == "__main__":
    execute()
