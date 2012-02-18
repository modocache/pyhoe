from pyhoe.utils.virtualenv import *

def test_virtualenv_available():
    assert virtualenv_available()

def test_virtualenvwrapper_available():
    assert virtualenvwrapper_available()

def test_check_env_for_package():
    assert check_env_for_package('pyhoe', 'nose')
