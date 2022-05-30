from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import os


testdata_file = os.path.join(os.path.dirname(__file__), 'data/testdata.json')


def test_ios_switches(init_driver):
    init_driver.find_element(By.ID, 'Switches').click()
    init_driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[2]').set_value('0')
    init_driver.back()

# def test_ios_steppers(init_driver):
#     init_driver.find_element(By.ID, 'Steppers').click()
#     el = init_driver.find_elements(AppiumBy.NAME, 'Increment')[1]
#     for i in range(0, 10):
#         el.click()
#     init_driver.back()

    # init_driver.find_element(By.ID, 'Sliders').click()
    # init_driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]').set_value('1')
    # init_driver.back()
    # init_driver.find_element(By.ID, 'Picker View').click()
    # init_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Red color component value').set_value('80')
    # init_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Green color component value').set_value('200')
    # init_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Blue color component value').set_value('100')
    # init_driver.background_app(-1)
    # init_driver.find_element(By.ID, 'Messages').click()
    # init_driver.find_elements(AppiumBy.NAME, 'Forward')[0].click()
    # init_driver.launch_app()

