from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def send_alert(driver):
    try:
        navigate_home = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Home")')
        navigate_home.click()
        click_alert = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(9)')
        click_alert.click()
        access1 = wait_for_element(driver,MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        if access1:
            access1.click()
        access2 = wait_for_element(driver,MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        if access2:
            access2.click()
        confirm_alert = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirm_alert.click()
        print("✅ Test Passed: Alert sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send alert")
        print(f"Error: {e}")
