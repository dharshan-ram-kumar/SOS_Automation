import time

from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def chat(driver):
    try:
        navigate_chat = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Chat")'
        )
        navigate_chat.click()
        click_control_room = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Control Room")',
        )
        click_control_room.click()
        type_chat = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Type a message...")',
        )
        type_chat.send_keys("Hello Control Room")
        send_chat = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send")'
        )
        send_chat.click()
        print("✅ Test Passed: Chat sent successful to the control room")

        send_location = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("").instance(1)',
        )
        send_location.click()
        time.sleep(5)
        print("✅ Test Passed: Live location sent successful to the control room")

    except Exception as e:
        print("❌ Test Failed: Unable to send message")
        print(f"Error: {e}")
