from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from data.picker_data import testdata


@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_picker(driver, data, go_dashboard):
    """
    This test aims to check Picker's page functionalities
    :param driver: parameter to request driver fixture
    :param go_dashboard: parameter to request go_dashboard fixture
    :param data: parameter of parametrized function to request testdata, stored separately from a test function
    :return:
    """
    driver.find_element(By.ID, 'Picker View').click()
    red_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Red color component value')
    green_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Green color component value')
    blue_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Blue color component value')
    red_el.set_value(data.red)
    green_el.set_value(data.green)
    blue_el.set_value(data.blue)
    red_el_value = red_el.get_attribute("value")
    green_el_value = green_el.get_attribute("value")
    blue_el_value = blue_el.get_attribute("value")
    assert int(red_el_value) == data.red and int(green_el_value) == data.green and int(blue_el_value) == data.blue
