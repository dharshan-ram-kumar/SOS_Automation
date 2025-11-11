from appium.webdriver.common.appiumby import AppiumBy
from utils.long_press import long_press
from utils.wait_for_element import wait_for_element


def send_alert(driver):
    try:
        navigate_home = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Home")'
        )
        navigate_home.click()
        # go_back = wait_for_element(
        #     driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'
        # )
        # if go_back:
        #     go_back.click()
        click_alert = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("SEND ALERT")',
        )
        long_press(driver, click_alert, duration=2)
        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
        print("✅ Test Passed: SOS alert sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send SOS alert")
        print(f"Error: {e}")
