from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from data.switches_data import testdata


@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_switches(driver, data, go_dashboard):
    """
    This test aims to check Switches' page functionalities
    :param driver: parameter to request driver fixture
    :param go_dashboard: parameter to request go_dashboard fixture
    :param data: parameter of parametrized function to request testdata, stored separately from a test function
    :return:
    """
    driver.find_element(By.ID, 'Switches').click()
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[2]').set_value(data.tinted)
    tinted_value = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[2]').get_attribute("value")
    assert int(tinted_value) == data.tinted
