from datetime import time
from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def admin_alert(driver):
    try:
        navigate_alert_page = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Alerts")')
        navigate_alert_page.click()
        live_monitor = wait_for_element(driver,MobileBy.ID,'new UiSelector().text("LIVE MONITOR").instance(0)')
        live_monitor.click()
        print("✅ Test Passed: Navigated to alert page")

    except Exception as e:
        print("❌ Test Failed: Unable to navigate to alert page")
        print(f"Error: {e}")
