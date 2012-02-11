import urllib2

# Test against Google IP
TEST_URL = "http://74.125.113.99"

def internet_connection_available():
    """docstring for internet_connection_available"""
    try:
        urllib2.urlopen(TEST_URL, timeout = 1)
        return True
    except urllib2.URLError:
        return False
    return False
