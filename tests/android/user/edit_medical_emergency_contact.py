import time
from appium.webdriver.common.appiumby import AppiumBy


def edit_medical_emergency_contact(driver):
    try:
        edit_contact = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(3)'
        )
        edit_contact.click()
        time.sleep(2)

        name = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Test")'
        )
        name.clear()
        type_name = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name")'
        )
        type_name.send_keys("Test1")
        time.sleep(2)

        relationship = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Relationship")'
        )
        relationship.clear()
        type_relationship = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Relationship")'
        )
        type_relationship.send_keys("Relationship1")
        time.sleep(2)

        number = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("9876543210")'
        )
        number.clear()
        type_number = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")'
        )
        type_number.send_keys("8765432190")

        save_contact = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Save")'
        )
        save_contact.click()
        time.sleep(2)

        contact_name = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Test1")'
        )
        contact_relationship = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Relationship1")',
        )
        contact_number = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("+91 8765432190")',
        )
        time.sleep(2)
        if contact_name and contact_relationship and contact_number:
            print("✅ Test Passed: Emergency contact updated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to update emergency contact")
        print(f"Error: {e}")
