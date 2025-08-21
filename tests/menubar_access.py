import time
from appium.webdriver.common.mobileby import MobileBy

def menu_access(driver):
    try:
        time.sleep(2)
        click_avatar = (driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(4)'))
        click_avatar.click()
        time.sleep(2)

    except Exception as e:
        print("❌ Test Failed: Unable to access menu bar")
        print(f"Error: {e}")
