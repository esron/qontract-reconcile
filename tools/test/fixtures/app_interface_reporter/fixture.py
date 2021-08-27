import os
import anymarkup
import pytest


@pytest.fixture
def path():
    return os.path.join(os.path.dirname(__file__), 'metrics.yml')


@pytest.fixture
def file(path):
    with open(path, 'r') as f:
        return f.read().strip()


@pytest.fixture
def get_anymarkup(file):
    return anymarkup.parse(file, force_types=None)


@pytest.fixture
def metrics(get_anymarkup):
    return get_anymarkup
