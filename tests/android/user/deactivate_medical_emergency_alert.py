import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def deactivate_medical_emergency_alert(driver):
    try:
        deactivate_alert = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("STOP ALERT")',
        )
        deactivate_alert.click()

        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
        print("✅ Test Passed: Medical emergency alert deactivated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to deactivate medical emergency alert")
        print(f"Error: {e}")
