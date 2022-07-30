import pytest

@pytest.fixture()
def name():
    return "devops univ"


def test_samplemethod(name):
    assert name == "devops univ"