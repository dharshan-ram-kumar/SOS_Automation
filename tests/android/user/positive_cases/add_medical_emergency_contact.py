import time
from appium.webdriver.common.appiumby import AppiumBy
from tests.android.user.positive_cases.menubar_access import menu_access


def add_medical_emergency_contact(driver):
    try:
        menu_access(driver)

        click_profile = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Profile")'
        )
        click_profile.click()
        add_contact = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add").instance(1)'
        )
        add_contact.click()
        time.sleep(2)

        type_name = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name")'
        )
        type_name.send_keys("Test")
        type_relationship = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Relationship")'
        )
        type_relationship.send_keys("Relationship")
        type_number = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")'
        )
        type_number.send_keys("9876543210")

        save_contact = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Add Contact")'
        )
        save_contact.click()
        time.sleep(2)

        success_message = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("android:id/button1")',
        )
        success_message.click()
        print("✅ Test Passed: Medical emergency contact added successful")

    except Exception as e:
        print("❌ Test Failed: Unable to add medical emergency contact")
        print(f"Error: {e}")
