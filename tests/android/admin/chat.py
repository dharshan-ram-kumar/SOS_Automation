from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def admin_chat(driver):
    try:
        navigate_chat = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Chats")',
        )
        navigate_chat.click()
        click_contact = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup").instance(9)',
        )
        click_contact.click()
        type_chat = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Type a message...")',
        )
        type_chat.send_keys("Hello")
        send_chat = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send")'
        )
        send_chat.click()
        print("✅ Test Passed: Chat sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send chat")
        print(f"Error: {e}")
