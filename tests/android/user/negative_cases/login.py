import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from utils.wait_for_element import wait_for_element


def login(driver, phone_number, password):
    try:
        time.sleep(2)
        try:
            time.sleep(2)
            deny_notification = wait_for_element(driver,
                AppiumBy.ID,
                "com.android.permissioncontroller:id/permission_deny_button",
            )
            if deny_notification:
                deny_notification.click()
            time.sleep(2)
            deny_notification = wait_for_element(driver,
                AppiumBy.ID,
                "com.android.permissioncontroller:id/grant_dialog",
            )
            if deny_notification.is_displayed():
                print("❌ Test Failed: Notification permission dialog is visible again")
            else:
                print("✅ Test Passed: Notification permission dialog is not visible again")
        except NoSuchElementException:
            pass
        deny_notification = wait_for_element(driver,
                                             AppiumBy.ID,
                                             "com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button",
                                             )
        if deny_notification:
            deny_notification.click()

        invalid_number = wait_for_element(driver,
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")'
        )
        invalid_number.send_keys("987654321")
        time.sleep(2)
        valid_password = wait_for_element(driver,
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter password")'
        )
        valid_password.send_keys(password)
        time.sleep(2)
        click_login_button = wait_for_element(driver,AppiumBy.ACCESSIBILITY_ID, "Login")
        click_login_button.click()

        validation_phone = wait_for_element(driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Phone number should be 10 digits for India")'
        )
        if validation_phone.is_displayed():
            print("✅ Test Passed: Validation error is visible under phone number field")
        else:
            print("❌ Test Failed: Validation error is not visible under phone number field")

        clear_number = wait_for_element(driver,
                                       AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("987654321")'
                                       )
        clear_number.clear()
        type_number = wait_for_element(driver,
                                       AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")'
                                       )
        type_number.send_keys(phone_number)
        time.sleep(2)
        clear_password = wait_for_element(driver,
                                         AppiumBy.ANDROID_UIAUTOMATOR,  'new UiSelector().textMatches("•+")'
                                         )
        clear_password.clear()
        type_password = wait_for_element(driver,
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter password")'
        )
        type_password.send_keys("Pass")
        click_login_button = wait_for_element(driver, AppiumBy.ACCESSIBILITY_ID, "Login")
        click_login_button.click()
        validation_password = wait_for_element(driver,AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Password must be at least 8 characters long")')
        if validation_password.is_displayed():
            print("✅ Test Passed: Validation error is visible under password field")
        else:
            print("❌ Test Failed: Validation error is not visible under password field")
        time.sleep(2)

        clear_password = wait_for_element(driver,
                                          AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("•+")'
                                          )
        clear_password.clear()
        type_password = wait_for_element(driver,
                                         AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter password")'
                                         )
        type_password.send_keys("Password")
        click_login_button = wait_for_element(driver, AppiumBy.ACCESSIBILITY_ID, "Login")
        click_login_button.click()

        error = wait_for_element(driver,AppiumBy.ID,"android:id/content")
        if error.is_displayed():
            print("✅ Test Passed: 'Invalid Credentials' error message is visible")
        else:
            print("❌ Test Failed: Error message not visible")

    except Exception as e:
        print("❌ Test Failed: Unable to test login negative flow")
        print(f"Error: {e}")
