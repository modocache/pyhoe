from __future__ import with_statement
import sys
from os import linesep
from os.path import join, dirname
import re
from fabric.api import abort, lcd, local, settings, task
from fabric.colors import red, yellow
from fabric.contrib.console import confirm
from fabric.utils import warn

DOC_DIR = "docs"
CONF_PATH = join(DOC_DIR, "conf.py")
INDEX_PATH = join(DOC_DIR, "_build/html/index.html")
SPHINX_CMD = "sphinx-quickstart"

@task(default=True)
def build(browse="no"):
    """
    Generate Sphinx documentation.
    """
    lazy_init_docs()
    with lcd("docs"):
        local("make html")
    if browse.lower() in ["yes", "y"]:
        view()

@task
def view():
    """
    Open the current dev docs in a browser tab.
    """
    lazy_init_docs()
    local("open %s" % INDEX_PATH)

@task
def delete():
    """Removes all docs from project."""
    if confirm(red(
        "Are you sure you want to remove your "
        "project documentation? This action CANNOT "
        "BE UNDONE."
    ), default = False):
        local("rm -rf docs")
    else:
        abort("Aborted on user request.")

@task
def reset():
    """
    Deletes, then builds documentation for project.
    """
    delete()
    build()

def lazy_init_docs():
    """
    Runs sphinx-quickstart if docs/conf.py does not exist yet.
    Advises user to install Sphinx if not found on PATH.
    """
    with settings(warn_only=True):
        doc_result = local("test -s %s" % CONF_PATH)
    if doc_result.failed:
        msg = (
            "It appears Sphinx documentation has "
            "not been made for this package yet. "
            "Would you like to make some now?"
        )
        if confirm(yellow(msg)):
            with settings(warn_only=True):
                sphinx_result = local("which -s %s" % SPHINX_CMD)
                docdir_result = local("test -d %s" % DOC_DIR)
            if sphinx_result.failed:
                abort(red(
                    "It appears Sphinx is not installed. Please "
                    "install Sphinx using `pip install Sphinx` and "
                    "try again."
                ))
            else:
                if docdir_result.failed:
                    local("mkdir %s" % DOC_DIR)
                with lcd(DOC_DIR):
                    local(SPHINX_CMD)
                # Add version sync mechanism for docs.
                add_version_sync()
                # Make HTML.
                build()
        else:
            warn(red(
                "Documentation not produced. Certain tasks may "
                "fail without documentation."
            ))

def add_version_sync():
    """
    Inserts project to system path so docs can use
    PROJECT_NAME.get_version() to update version.
    """
    with open(CONF_PATH) as f:
        project_name = ""
        r = re.compile("^project = u")
        lines = f.readlines()
        for line in lines:
            if r.match(line):
                project_name = line[len("project = u\""):-2]

        # Make sure bundle implements get_version()
        try:
            sys.path.insert(0, dirname(dirname(__file__)))
            __import__(project_name)
        except ImportError:
            warn(red(
                "Could not import project named %s" % project_name
            ))
            return
        try:
            __import__(project_name).get_version()
        except NameError:
            warn(red(
                "%s does not have a get_version() method." % project_name
            ))
            return

        r = re.compile("import sys")
        r_ver = re.compile("^version = ")
        r_rel = re.compile("^release = ")
        for i, line in enumerate(lines):
            if r.match(line):
                lines.insert(
                    i+1,
                    "sys.path.insert(0, os.path.abspath('..'))" + linesep
                )
                lines.insert(i+2, ("import %s%s" % (project_name, linesep)))
            elif r_ver.match(line):
                lines[i] = \
                    "version = %s.get_version()%s" % (project_name, linesep)
            elif r_rel.match(line):
                lines[i] = \
                    "release = %s.get_version()%s" % (project_name, linesep)
    with open(CONF_PATH, "w") as f:
       f.write("".join(lines))
