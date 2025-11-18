import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def deactivate_alert(driver):
    try:
        time.sleep(20)
        deactivate_alerts = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("STOP SOS ALERT")',
        )
        deactivate_alerts.click()
        print("✅ Test Passed: SOS alert deactivated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to deactivate SOS alert")
        print(f"Error: {e}")
