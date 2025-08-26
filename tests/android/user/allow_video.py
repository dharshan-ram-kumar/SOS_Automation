from appium.webdriver.common.mobileby import MobileBy
from tests.android.user.menubar_access import menu_access
from tests.android.user.send_alert import send_alert

def allow_video(driver):
    try:
        menu_access(driver)
        access = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Switch").instance(4)')
        access.click()
        print("✅ Test Passed: Video access disabled successful")
        close_menu = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("")')
        close_menu.click()
        send_alert(driver)
    except Exception as e:
        print("❌ Test Failed: Unable to send alert")
        print(f"Error: {e}")
