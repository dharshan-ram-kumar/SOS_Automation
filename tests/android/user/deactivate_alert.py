import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.long_press import long_press
from utils.wait_for_element import wait_for_element


def deactivate_alert(driver):
    try:
        time.sleep(15)
        deactivate_alerts = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("STOP SOS ALERT")',
        )
        deactivate_alerts.click()
        print("✅ Test Passed: Alert deactivated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to deactivate alert")
        print(f"Error: {e}")
