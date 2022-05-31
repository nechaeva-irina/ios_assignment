from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from data.steppers_data import testdata


@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_steppers(driver, data, go_dashboard):
    """
    This test aims to check Steppers' page functionalities
    :param driver: parameter to request driver fixture
    :param go_dashboard: parameter to request go_dashboard fixture
    :param data: parameter of parametrized function to request testdata, stored separately from a test function
    :return:
    """
    driver.find_element(By.ID, 'Steppers').click()
    el = driver.find_elements(AppiumBy.NAME, 'Increment')[1]
    for i in range(0, data.tinted):
        el.click()
    assert driver.find_element(AppiumBy.ID, str(data.tinted))
