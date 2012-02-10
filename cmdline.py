#!/usr/bin/env python

import os, sys
import subprocess
import builder

class InvalidCommandException(Exception):
    """
    An exception raised when an argument supplied
    is not valid.
    """
    def __init__(self, serial, msg):
        self.serial = serial
        self.msg = msg
    def __str__(self):
        return "[Errno %d] %s" % (self.serial, self.msg)


class CommandLineDelegator(object):
    """
    Performs commands based on arguments provided.
    Also handles validation of arguments supplied
    from the command line.
    """
    def __init__(self, args):
        self.args = args

    def execute(self):
        """
        Cleans and packs command line arguments and passes
        them to ProjectBuilder.
        """
        self.clean_args()
        build_args = {
            "project_name": self.args["project_name"],
            "template": self.args["template"],
            "skip_confirmation": self.args["yes_to_all"]
        }
        if self.args["python_exe"]:
            build_args = dict(
                build_args.items() + ("python_exe", self.args["python_exe"])
            )
        p = builder.ProjectBuilder()
        p.build(**build_args)


    def clean_args(self):
        """
        Loops over arguments provided and calls a validation
        method for each, if one exists. If a validation method
        does not exist, no validation is performed.
        """
        for key, val in self.args.items():
            try:
                # Validate input for key.
                clean_function = getattr(self, "clean_%s" % key.lower())
                if val: clean_function(val)
            except AttributeError:
                # No clean method for key.
                pass

    def clean_project_name(self, project_name):
        """
        Validates input for project_name.
        """
        if project_name in os.listdir(os.getcwd()):
            errmsg = (
                "A directory named `%s` already exists in this directory. "
                "Choose a different project name and try again."
                % project_name
            )
            raise InvalidCommandException(1, errmsg)

    def clean_python_exe(self, python_exe):
        """
        Validates input for python_exe.
        """
        try:
            # FIXME - Prevent shell from writing to stdout.
            sys.stderr.write("Checking for %s...\n" % python_exe)
            subprocess.check_call("which %s" % python_exe, shell=True)
            sys.stderr.write("OK!\n")
        except subprocess.CalledProcessError:
            errmsg = (
                "The Python executable you specified does not "
                "seem to be on your path."
            )
            raise InvalidCommandException(2, errmsg)
