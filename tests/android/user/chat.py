from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def chat(driver):
    try:
        navigate_chat = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Chat")')
        navigate_chat.click()
        click_control_room = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Control Room")')
        click_control_room.click()
        type_chat = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type a message...")')
        type_chat.send_keys("Hello Control Room")
        send_chat = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send")')
        send_chat.click()
        print("✅ Test Passed: Chat sent successful")

        send_location = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(1)')
        send_location.click()
        print("✅ Test Passed: Live location sent successful")

    except Exception as e:
        print("❌ Test Failed: Unable to send message")
        print(f"Error: {e}")
