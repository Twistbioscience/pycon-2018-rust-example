from os import path

import pytest

from is_blank import is_blank, is_blank_py, is_blank_py_naive

cwd = path.abspath(path.dirname(__file__))

LENGTH = 100 * 1000000


# left disabled as takes a while to run
def _test_is_blank_PY_naive(benchmark):
    filepath = path.join(cwd, f'fixture_blank_{LENGTH}.txt')
    assert benchmark(is_blank_py_naive, filepath)


def test_is_blank_PY(benchmark):
    filepath = path.join(cwd, f'fixture_blank_{LENGTH}.txt')
    assert benchmark(is_blank_py, filepath)


def test_is_blank_RUST(benchmark):
    filepath = path.join(cwd, f'fixture_blank_{LENGTH}.txt')
    assert benchmark(is_blank, filepath)
