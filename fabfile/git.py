from __future__ import with_statement
from os.path import dirname, join
from fabric.api import abort, cd, local, settings, task
from fabric.colors import red, green, yellow
from fabric.contrib.console import confirm

CODE_DIR = dirname(dirname(__file__))

@task
def commit():
    """Commits files."""
    confirm_message = yellow("%s is not a git repository. Would you"
    "like to initialize it as one?" % CODE_DIR)
    if local("test -d %s" % join(CODE_DIR, ".git")).failed and \
        not confirm(confirm_message):
        local("git init")

    # local("git add --patch && git commit")
    local("git status")

