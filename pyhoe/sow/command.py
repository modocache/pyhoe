#!/usr/bin/env python
import os, sys
import argparse
from pyhoe.utils import git
from pyhoe.sow.delegator import SowCommandDelegator

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

def default_template():
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
    author_name = (
        git.get_config_value("github.name") or
        git.get_config_value("user.name")
    )

    parser = argparse.ArgumentParser(
        prog="pyhoe sow",
        description = (
            "Initializes a Python project using established best practices."
        )
    )
    parser.add_argument(
        "project_name",
        help = "The name of the project."
    )
    parser.add_argument(
        "-a", "--author_name",
        default = author_name,
        help = (
            "Your name. If not specified, the values in "
            "your global gitconfig will be used."
        )
    )
    parser.add_argument(
        "-e", "--email",
        dest = "author_email",
        default = git.get_config_value("user.email"),
        help = (
            "Your email address. If not "
            "specified, the values in your global gitconfig "
            "will be used."
        )
    )
    # TODO
    # parser.add_argument(
    #     "-c", "--cucumber",
    #     action = "store_true",
    #     help = "Use freshen for behavior-driven development."
    # )
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
        default = default_template(),
        help = "The template to use for your project."
    )
    parser.add_argument(
        "-y", "--yes-to-all",
        action = "store_true",
        help = (
            "Skip all confirmation and use recommended settings."
        )
    )

    if len(sysargs) <= 0:
        parser.print_help()
        sys.exit(0)

    return vars(parser.parse_args(sysargs))


def execute(args):
    """
    Parses sys.args or args parameter and executes
    the parsed values using CommandLineDelegator.
    """
    delegator = SowCommandDelegator(parse(args))
    delegator.dispatch()


if __name__ == "__main__":
    execute(sys.argv)
