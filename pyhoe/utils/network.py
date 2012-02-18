try:
    from urllib2 import urlopen, URLError
except ImportError:
    # urllib2 has been merged into urllib as of Python 3.0
    # http://docs.python.org/release/3.2.2/whatsnew/3.0.html?highlight=urllib2#library-changes
    from urllib.request import urlopen
    from urllib.error import URLError

# Test against Google IP
TEST_URL = "http://74.125.113.99"

def internet_connection_available():
    """
    Determines whether an internet connection is
    available by polling a test URL.
    """
    try:
        urlopen(TEST_URL, timeout = 1)
        return True
    except URLError:
        return False
    return False
