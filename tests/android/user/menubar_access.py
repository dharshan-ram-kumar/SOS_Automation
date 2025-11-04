import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def menu_access(driver):
    try:
        time.sleep(2)
        click_avatar = wait_for_element(driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup").instance(6)',
        )
        click_avatar.click()
        time.sleep(2)

    except Exception as e:
        print("❌ Test Failed: Unable to access menu bar")
        print(f"Error: {e}")
