from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element
from appium.webdriver.common.touch_action import TouchAction

def send_alert(driver):
    try:
        navigate_home = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Home")'
        )
        navigate_home.click()
        click_alert = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("SEND ALERT")',
        )
        action = TouchAction(driver)
        action.long_press(el=click_alert, duration=3000).release().perform()
        confirm_alert = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirm_alert.click()
        print("✅ Test Passed: Alert sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send alert")
        print(f"Error: {e}")
