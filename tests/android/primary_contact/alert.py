from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def alert_pc(driver):
    try:
        navigate_alert_page = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Alerts")'
        )
        navigate_alert_page.click()
        verify_active = wait_for_element(driver,AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("ACTIVE").instance(0)')
        if verify_active:
            print("✅ Test Passed: Active alert found in alert page")
        else:
            print("❌ Test Failed: No active alert found in alert page")

    except Exception as e:
        print("❌ Test Failed: Unable to navigate to alert page")
        print(f"Error: {e}")
