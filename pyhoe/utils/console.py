import sys

def confirm(question, default = True):
    """
    Prompts the user for confirmation with the given default.
    """
    if default:
        suffix = "[Y/n]"
    else:
        suffix = "[y/N]"

    while True:
        sys.stdout.write("%s %s: " % (question, suffix))
        response = raw_input().lower()
        if not response:
            return default
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        sys.stdout.write("I don't understand. Please specify (y)es or (n)o.")
