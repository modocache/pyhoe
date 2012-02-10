from os import listdir
from os.path import dirname, splitext
import re

r = re.compile("^[a-zA-Z0-9]*\.py$")

__all__ = [
    splitext(m)[0]for m in listdir(dirname(__file__)) if r.match(m)
]
