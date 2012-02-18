from nose.tools import *
import PROJECT_NAME

def setup():
    """Setup tests."""
    pass

def teardown():
    """Tear down tests."""
    pass

def test_get_version():
    assert type(PROJECT_NAME.get_version()) == str
