from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from data.sliders_data import testdata


@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_sliders(driver, data, go_dashboard):
    """
    This test aims to check Sliders' page functionalities
    :param driver: parameter to request driver fixture
    :param go_dashboard: parameter to request go_dashboard fixture
    :param data: parameter of parametrized function to request testdata, stored separately from a test function
    :return:
    """
    driver.find_element(By.ID, 'Sliders').click()
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]').set_value(data.tinted)
    el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]')
    el_value = el.get_attribute("value")
    assert el_value == "{:.0%}".format(data.tinted)
