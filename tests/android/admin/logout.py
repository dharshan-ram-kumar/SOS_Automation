from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def admin_logout(driver):
    try:
        click_logout = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Logout")'
        )
        click_logout.click()
        confirm_logout = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_logout.click()
        print("✅ Test Passed: Logout successful")

    except Exception as e:
        print("❌ Test Failed: Unable to logout")
        print(f"Error: {e}")
