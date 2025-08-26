from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def admin_logout(driver):
    try:
        click_logout= wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Logout")')
        click_logout.click()
        confirm_logout = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirm_logout.click()
        print("✅ Test Passed: Logout successful")

    except Exception as e:
        print("❌ Test Failed: Unable to logout")
        print(f"Error: {e}")
