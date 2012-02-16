from __future__ import with_statement
import os
from os.path import dirname
from fabric.api import abort, local, settings, task
from fabric.colors import yellow
from fabric.contrib.console import confirm

TEST_DIR = "tests"
DEFAULT_PROJECT_NAME = "PROJECT_NAME"
DIR_PROJECT_NAME = dirname(dirname(__file__)).split(os.sep)[-1]

def init(name=None):
    """
    Initializes a project.
    """
    with settings(warn_only=True):
        # Create project dir, test dir and file.
        if not name:
            name = DIR_PROJECT_NAME
            if not confirm(yellow(
                "Project will be initialized with the name "
                "`%s`, is this OK?" % name
            )):
                abort(
                    "You can specify a name by passing it as an "
                    "argument as in `fab project.init:prj_name`."
                )
        dir_test = local("test -d %s" % DEFAULT_PROJECT_NAME)
        if not dir_test.failed:
            local("mv %s %s" % (DEFAULT_PROJECT_NAME, name))

        # Create tests directory if one doesn't already exist.
        testdir_test = local("test -d %s" % TEST_DIR)
        if testdir_test.failed:
            local("mkdir %s && touch %s/__init__.py" % (TEST_DIR, TEST_DIR))

        # Create test file if one doesn't exist. 
        testfile_test = local(
            "test -e %s/%s_tests.py" % (TEST_DIR, DEFAULT_PROJECT_NAME)
        )
        if testfile_test.failed:
            local("touch tests/%s_tests.py" % DEFAULT_PROJECT_NAME)
        tfp = os.path.join(TEST_DIR, "%s_tests.py")
        local("mv %s %s" % (tfp % DEFAULT_PROJECT_NAME, tfp % name))


def init_setuptools(name):
    """
    Configures setup.py for the project.
    """
    # TODO - Not yet implemented.
    pass


def create_tarball():
    """docstring for create_tarball"""
    # TODO - Not yet implemented.
    pass


