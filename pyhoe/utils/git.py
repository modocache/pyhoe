import os
import subprocess
import re

def check_for_git(function):
    """
    Makes sure git is installed on the system.
    Returns None if it is not.
    """
    def _check_for_git(*args, **kwargs):
        try:
            subprocess.check_call(
                "git config --global --list &> /dev/null",
                shell=True
            )
        except subprocess.CalledProcessError:
            return None
        return function(*args, **kwargs)
    return _check_for_git


@check_for_git
def get_global_config():
    return bytes.decode(
        subprocess.check_output(
            "git config --global --list",
            stderr = subprocess.STDOUT,
            shell = True
        )
    )

@check_for_git
def get_config_value(val):
    """
    Returns global gitconfig value.
    Ex.: get_config_value("user.email") returns
         email registered in gitconfig.
    """
    m = re.search(
        "%s?%s=(.*)%s" % (os.linesep, val, os.linesep),
        get_global_config()
    )
    if m:
        try:
            return m.group(1)
        except IndexError:
            pass
    return None

@check_for_git
def git_init():
    """Runs git init."""
    subprocess.call("git init", shell=True)
