from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def send_alert(driver):
    try:
        navigate_home = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Home")')
        navigate_home.click()
        click_alert = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(9)')
        click_alert.click()
        confirm_alert = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirm_alert.click()
        print("✅ Test Passed: Alert sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send alert")
        print(f"Error: {e}")
