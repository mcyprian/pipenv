try:
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportEror:
    from urllib import urlopen
    URLError = IOError

import pytest


def are_we_connected():
    try:
        urlopen('http://python.org')
        return True
    except URLError:
        return False


connection_required = pytest.mark.skipif(
    not are_we_connected(),
    reason="An internet connection is required")
