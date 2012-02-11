import sys, os
from os.path import join, dirname
import subprocess
import shutil
import re
from pyhoe.startproject.command import TEMPLATE_DIR
from pyhoe.utils import virtualenv, git
from pyhoe.utils.console import confirm

# FIXME - Place this in utils module.
def color_terminal():
    """
    Returns True if terminal supports colored output,
    False otherwise.
    """
    if not hasattr(sys.stdout, 'isatty'):
        return False
    if not sys.stdout.isatty():
         return False
    if 'COLORTERM' in os.environ:
        return True
    term = os.environ.get('TERM', 'dumb').lower()
    if term in ('xterm', 'linux') or 'color' in term:
        return True
    return False

def describe(path, action="created"):
    """
    Describes the action being performed.
    """
    relpath = os.path.relpath(path)
    if color_terminal():
        if action == "created":
            print "%s...created %s%s" % ("\033[32m", relpath, "\033[0m")
    else:
        if action == "created":
            print "...created %s" % relpath

DEFAULT_PACKAGES = ["nosy", "sneazr", "tox", "Fabric"]

def execute(
    project_name,
    template,
    author_name=None,
    author_email=None,
    cucumber=False,
    python_exe=None,
    yes_to_all=False
):
    # Copy template.
    shutil.copytree(join(TEMPLATE_DIR, template), project_name)

    # Rename template project name.
    PLACEHOLDERS = [
        "PROJECT_NAME",
        "AUTHOR_NAME",
        "AUTHOR_EMAIL",
    ]
    proj_name_regex = re.compile("%s" % PLACEHOLDERS[0])
    for root, dirs, files in os.walk(project_name):
        for d in dirs:
            os.rename(
                join(root, d),
                join(root, re.sub(proj_name_regex, project_name, d))
            )
        for f in files:
            # Replace various values in files.
            settings = [project_name, author_name, author_email]
            for i, setting in enumerate(settings):
                if setting is not None:
                    r = re.compile(PLACEHOLDERS[i])
                    data = ""
                    with open(join(root, dirname(f), f), "r") as read_file:
                        data = re.sub(r, setting, read_file.read())
                    with open(join(root, dirname(f), f), "w") as write_file:
                        write_file.write(data)

            # Rename any files with PROJECT_NAME in them.
            os.rename(
                join(root, dirname(f), f),
                join(root, dirname(f), re.sub(r, project_name, f))
            )

    # Display what was created.
    for root, dirs, files in os.walk(project_name):
        describe(root)
        for d in dirs:
            describe(join(root, d))
        for f in files:
            describe(join(root, dirname(f), f))

    # Create virtualenv
    packages_to_install = []
    if virtualenv.virtualenvwrapper_available():
        if (
            yes_to_all or
            confirm("Create virtualenv %s for this project?" % project_name)
        ):
            # Determine packages to install.
            if (
                yes_to_all or
                confirm(
                    "Install recommended packages to virtualenv %s?"
                    % project_name
                )
            ):
                for package in DEFAULT_PACKAGES:
                    packages_to_install.append(package)

            # Check for documentation.
            if (
                yes_to_all or
                confirm("Create documentation for %s?" % project_name)
            ):
                packages_to_install.append("Sphinx")

            virtualenv.mkvirtualenv(
                project_name,
                packages_to_install
            )
    elif virtualenv.virtualenv_available():
        vpath = join(project_name, ".%s" % project_name)
        if (
            yes_to_all or
            confirm("Create virtualenv %s for this project?" % vpath)
        ):
            os.chdir(join(os.getcwd(), project_name))
            # Create a virtualenv in the project directory.
            # FIXME - Not sure if this is a good idea, I've never
            # used virtualenv without virtualenvwrapper.
            virtualenv.mkvirtualenv(
                ".%s" % project_name,
                env_dir = project_name
            )

    # Change to project dir
    os.chdir(join(os.getcwd(), project_name))

    # Initialize git repository.
    if (
        yes_to_all or
        confirm("Initialize git repository for this project?")
    ):
        git.git_init()

    if virtualenv.check_env_for_package(project_name, "Sphinx"):
        os.mkdir("docs")
        os.chdir("docs")
        subprocess.call("sphinx-quickstart", shell=True)

