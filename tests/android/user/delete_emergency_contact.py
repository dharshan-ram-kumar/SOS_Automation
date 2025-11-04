import time
from appium.webdriver.common.appiumby import AppiumBy


def delete_emergency_contact(driver):
    try:
        delete_contact = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'
        )
        delete_contact.click()
        time.sleep(2)

        confirm = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("android:id/button1")',
        )
        confirm.click()

        contact_name = driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Test1")'
        )
        contact_relationship = driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Relationship1")',
        )
        contact_number = driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("+91 8765432190")',
        )

        if not contact_name and not contact_relationship and not contact_number:
            print("✅ Test Passed: Emergency contact deleted successful")

    except Exception as e:
        print("❌ Test Failed: Unable to delete emergency contact")
        print(f"Error: {e}")
