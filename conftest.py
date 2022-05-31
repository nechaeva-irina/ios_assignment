import pytest
from appium import webdriver
import json
import os.path
import warnings

fixture = None


@pytest.fixture(scope="session")
def driver():
    """
    Function for fixture and driver initialization.
    :return: fixture
    """
    global fixture
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
    with open(config_file) as f:
        target = json.load(f)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        fixture = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=target)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    """
    Function to destroy fixture in the end of tests execution
    :param request: special parameter of pytest framework
    :return:
    """

    def fin():
        fixture.quit()
    request.addfinalizer(fin)


@pytest.fixture(scope="function")
def go_dashboard():
    """
    Function to go back to the dashboard after each test
    :return:
    """
    fixture.back()
