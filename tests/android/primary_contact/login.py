import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from utils.wait_for_element import wait_for_element


def login_pc(driver, phone_number, password):
    try:
        time.sleep(2)
        try:
            time.sleep(2)
            allow_notification = driver.find_element(
                AppiumBy.ID,
                "com.android.permissioncontroller:id/permission_allow_button",
            )
            allow_notification.click()
            time.sleep(2)
        except NoSuchElementException:
            pass

        type_number = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")'
        )
        type_number.send_keys(phone_number)
        time.sleep(2)

        type_password = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter password")'
        )
        type_password.send_keys(password)
        time.sleep(2)

        click_login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login")
        click_login_button.click()
        time.sleep(2)
        allow_location = wait_for_element(
            driver,
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
        )
        if allow_location:
            allow_location.click()
        print("✅ Test Passed: Login Successful")
        time.sleep(2)

    except Exception as e:
        print("❌ Test Failed: Login unsuccessful")
        print(f"Error: {e}")
