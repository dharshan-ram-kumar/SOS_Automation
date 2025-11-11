from appium.webdriver.common.appiumby import AppiumBy
from tests.android.user.positive_cases.menubar_access import menu_access
from utils.long_press import long_press
from utils.wait_for_element import wait_for_element


def send_alert_safe_mode(driver):
    try:
        menu_access(driver)
        access = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.Switch").instance(4)',
        )
        access.click()
        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
        print("✅ Test Passed: Safe mode enabled successful")
        close_menu = wait_for_element(driver,AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        close_menu.click()

        click_alert = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("SEND ALERT")',
        )
        long_press(driver, click_alert, duration=2)
        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
        print("✅ Test Passed: Tried to send alert after enabled safe mode")

        menu_access(driver)
        access = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.Switch").instance(4)',
        )
        access.click()
        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
    except Exception as e:
        print("❌ Test Failed: Unable to enable safe mode or able to send alert in safe mode")
        print(f"Error: {e}")
