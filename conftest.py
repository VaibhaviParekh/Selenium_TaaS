import pytest

# pytest_plugins = ['pytest_selenium']

def pytest_addoption(parser):
    parser.addoption("--agency", action="store", default="", help="User Name to login")
    parser.addoption("--user", action="store", default="", help="User Name to login")
    parser.addoption("--password", action="store", default='Pertino!@#', help="Account password for test")


@pytest.fixture(scope="session", autouse=True)
def cmdopt(request):
    cmdopt = {}
    cmdopt['agency'] = request.config.getoption("--agency")
    cmdopt['user'] = request.config.getoption("--user")
    cmdopt['pwd'] = request.config.getoption("--password")

