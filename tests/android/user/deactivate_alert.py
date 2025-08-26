from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def deactivate_alert(driver):
    try:
        deactivate_alerts = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(9)')
        deactivate_alerts.click()
        confirmation = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirmation.click()
        print("✅ Test Passed: Alert deactivated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to deactivate alert")
        print(f"Error: {e}")
