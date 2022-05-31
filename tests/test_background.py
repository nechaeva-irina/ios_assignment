from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


def test_background(driver, go_dashboard):
    """
    This test is to check moving the app into the background, opening another app and returning to the previous app.
    :param driver: parameter to request driver fixture
    :param go_dashboard: parameter to request go_dashboard fixture
    :return:
    """
    driver.background_app(-1)
    driver.find_element(By.ID, 'Messages').click()
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'ConversationList')
        driver.find_element(AppiumBy.NAME, 'OK').click()
    except NoSuchElementException:
        pass
    try:
        driver.find_elements(AppiumBy.NAME, 'Forward')[0].click()
        driver.launch_app()
    except IndexError:
        driver.back()
        driver.find_elements(AppiumBy.NAME, 'Forward')[0].click()
        driver.launch_app()
    assert driver.find_element(AppiumBy.NAME, 'UIKitCatalog')
