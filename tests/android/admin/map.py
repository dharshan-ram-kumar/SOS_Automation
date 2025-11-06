from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def admin_map(driver):
    try:
        navigate_map = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Maps")'
        )
        navigate_map.click()
        allow_location = wait_for_element(
            driver,
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
        )
        if allow_location:
            allow_location.click()
        print("✅ Test Passed: Navigated to map page")

    except Exception as e:
        print("❌ Test Failed: Unable to navigate to map page")
        print(f"Error: {e}")
