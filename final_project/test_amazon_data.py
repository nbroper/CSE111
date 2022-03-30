from amazon_data import read_dict
from os import path
from tempfile import mktemp
from pytest import approx
import pytest


def test_read_dict():
    