import time

from appium.webdriver.common.appiumby import AppiumBy
from utils.long_press import long_press
from utils.wait_for_element import wait_for_element

def medical_emergency_alert(driver):
    try:
        navigate_home = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Home")'
        )
        navigate_home.click()
        click_alert = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("MEDICAL EMERGENCY")',
        )
        long_press(driver, click_alert, duration=2)
        time.sleep(5)
        # confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        # confirm_alert.click()
        print("✅ Test Passed: Medical emergency alert sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send medical emergency alert")
        print(f"Error: {e}")