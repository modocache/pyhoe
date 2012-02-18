from pyhoe.utils import network

def test_internet_connection_available():
    assert network.internet_connection_available()
