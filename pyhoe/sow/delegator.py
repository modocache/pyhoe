import os
import subprocess
from pyhoe.delegator import BaseCommandDelegator, InvalidCommandException

class SowCommandDelegator(BaseCommandDelegator):
    """
    Validates commands for startproject.
    """
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
            subprocess.check_call(
                "which %s &> /dev/null" % python_exe, shell=True
            )
        except subprocess.CalledProcessError:
            errmsg = (
                "The Python executable you specified does not "
                "seem to be on your path."
            )
            raise InvalidCommandException(2, errmsg)
