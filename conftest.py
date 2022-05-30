import pytest
from appium import webdriver
import json

target = None

@pytest.fixture(scope='session')
def des_cap():
  with open('data/desired_capabilities.json') as desired_capabilities:
    data = json.load(desired_capabilities)
  return data

@pytest.fixture(scope="session")
def init_driver(request):
    global fixture
    global target
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    fixture = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=target["iOS"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def tearDown(request):
    def fin():
        fixture.quit()
    yield
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
