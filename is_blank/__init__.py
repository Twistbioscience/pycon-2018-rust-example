import re

from ._fast_is_blank import is_blank

__all__ = ['is_blank', 'is_blank_py', 'is_blank_py_naive']

BLANK_RE = re.compile(r'^\s*$')


def is_blank_py(filepath):
    with open(filepath, "r") as f:
        return BLANK_RE.match(f.read()) is not None


def is_blank_py_naive(filepath):
    with open(filepath, "r") as f:
        for c in f.read():
            if c != " ":
                return False
        return True
