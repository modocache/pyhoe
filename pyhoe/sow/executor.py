import os
from os.path import join, dirname
import subprocess
import shutil
import re
from pyhoe.sow.command import TEMPLATE_DIR
from pyhoe.utils import virtualenv, git
from pyhoe.utils.console import confirm, print_green, print_yellow

DEFAULT_PACKAGES = ["nose", "nosy", "coverage", "sneazr", "tox"]

def describe(path, action="created"):
    """Describes the action being performed."""
    if action == "created":
        print_green("...created %s\n" % os.path.relpath(path))
    elif action == "moved":
        print_yellow("cd %s" % os.path.abspath(path))

def execute(
    project_name,
    template,
    author_name=None,
    author_email=None,
    cucumber=False,
    python_exe=None,
    yes_to_all=False
):
    # Confirm options
    should_create_virtualenv = should_install_packages = \
    should_create_docs = should_git_init = yes_to_all
    if not yes_to_all:
        should_create_virtualenv = confirm(
            "Create virtualenv %s for this project?" % project_name
        )
        should_install_packages = (
            should_create_virtualenv and
            virtualenv.virtualenvwrapper_available() and
            confirm(
                "Install recommended packages to virtualenv %s?"
                % project_name
            )
        )
        should_create_docs = (
            should_install_packages and
            confirm("Create documentation for %s?" % project_name)
        )
        should_git_init = confirm(
            "Initialize git repository for this project?"
        )

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
                join(
                    root, dirname(f),
                    re.sub(PLACEHOLDERS[0], project_name, f)
                )
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
        if should_create_virtualenv:
            # Determine packages to install.
            if should_install_packages:
                for package in DEFAULT_PACKAGES:
                    packages_to_install.append(package)

            # Check for documentation.
            if should_create_docs:
                packages_to_install.append("Sphinx")

            virtualenv.mkvirtualenv(
                name = project_name,
                python_exe = python_exe,
                packages_to_install = packages_to_install
            )
    elif virtualenv.virtualenv_available():
        if should_create_virtualenv:
            os.chdir(join(os.getcwd(), project_name))
            # Create a virtualenv in the project directory.
            # FIXME - Not sure if this is a good idea, I've never
            # used virtualenv without virtualenvwrapper.
            virtualenv.mkvirtualenv(
                name = ".%s" % project_name,
                python_exe = python_exe,
                env_dir = project_name
            )

    # Change to project dir
    os.chdir(join(os.getcwd(), project_name))

    # Initialize git repository.
    if should_git_init:
        git.git_init()

    # FIXME - Should create some way for templates to implement their
    # own logic.
    if should_create_docs:
        docdir = "docs"
        os.mkdir(docdir)
        os.chdir(docdir)
        subprocess.call("sphinx-quickstart", shell=True)

