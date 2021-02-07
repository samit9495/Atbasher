import pytest

def pytest_addoption(parser):
    parser.addoption("--file", type=str, nargs='+')


@pytest.fixture
def filename(request):
    return request.config.getoption("--file")