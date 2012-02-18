import sys, os

def is_color_terminal():
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

def color_stdout(message, color):
    """
    Writes to stdout in the specified color if color
    is supported in the terminal.
    """
    if is_color_terminal():
        sys.stdout.write("\033[%sm%s\033[0m" % (str(color), message))
    else:
        sys.stdout.write(message)

def print_red(message):
    color_stdout(message, 31)
def print_green(message):
    color_stdout(message, 32)
def print_yellow(message):
    color_stdout(message, 33)


def confirm(question, default = True):
    """
    Prompts the user for confirmation with the given default.
    """
    if default:
        suffix = "[Y/n]"
    else:
        suffix = "[y/N]"

    while True:
        print_yellow("%s %s: " % (question, suffix))
        # FIXME - Replace with sys.stdin.readline()
        try:
            response = raw_input().lower()
        except NameError:
            # raw_input() was merged into input() in Python 3.0.
            # See: http://www.python.org/dev/peps/pep-3111
            response = input().lower()
        if not response:
            return default
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        print_red("I don't understand. Please specify (y)es or (n)o.\n")
