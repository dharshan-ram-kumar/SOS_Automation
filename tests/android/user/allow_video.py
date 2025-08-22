from appium.webdriver.common.mobileby import MobileBy
from tests.android.user import menubar_access
from tests.android.user.send_alert import send_alert

def allow_video(driver):
    try:
        menubar_access(driver)
        allow_video = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Switch").instance(4)')
        allow_video.click()
        print("✅ Test Passed: Video access disabled successful")
        close_menu = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("")')
        close_menu.click()
        send_alert(driver)
    except Exception as e:
        print("❌ Test Failed: Unable to send alert")
        print(f"Error: {e}")
