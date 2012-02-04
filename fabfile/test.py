from __future__ import with_statement
from os.path import dirname
from fabric.api import abort, cd, local, settings, task
from fabric.colors import red, green
from fabric.contrib.console import confirm

CODE_DIR = dirname(dirname(__file__))

@task(default=True)
def test():
    """Runs tests."""
    install_nosetests_msg = ("It appears you do not have nosetests "
    "installed. Please install nosetests using `pip install "
    "nosetests` and try again.")
    if local("which -s nosetests").return_code == 1:
        abort(install_nosetests_msg)

    with cd(CODE_DIR):
        with settings(warn_only=True):
            result = local("nosetests", capture=True)
        if result.failed:
            if not confirm(
                red("Tests failed. Continue anyway?"),
                default=False
            ):
                abort("Aborting at user request.")
        else:
            print(green("All tests passed!"))
