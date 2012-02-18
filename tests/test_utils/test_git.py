import re
from pyhoe.utils import git

def test_get_global_config():
    config = git.get_global_config()
    assert config is not None
    assert re.search('user.name', config) is not None

def test_get_config_value():
    username = git.get_config_value('user.name')
    assert len(username) > 0
