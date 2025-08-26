from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def admin_map(driver):
    try:
        navigate_map = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Maps")')
        navigate_map.click()
        allow_location = wait_for_element(driver,MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        allow_location.click()
        print("✅ Test Passed: Navigated to map page")

    except Exception as e:
        print("❌ Test Failed: Unable to navigate to map page")
        print(f"Error: {e}")
