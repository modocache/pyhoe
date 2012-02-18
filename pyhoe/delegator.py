import os

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


class BaseCommandDelegator(object):
    """
    Performs commands based on arguments provided.
    Also handles validation of arguments supplied
    from the command line.
    """
    def __init__(self, args):
        self.args = args

    def dispatch(self, command_name=None):
        """
        Cleans and packs command line arguments and passes
        them to ProjectBuilder.
        """
        self.clean_args()
        if command_name is None:
            command_name = \
                self.__class__.__name__[:-len("CommandDelegator")].lower()
        __import__(
            "%s.%s.executor" % ("pyhoe", command_name),
            fromlist = ["pyhoe"]
        ).execute(**self.args)

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
