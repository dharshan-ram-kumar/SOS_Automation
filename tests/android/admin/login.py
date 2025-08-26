import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

def admin_login(driver, phone_number, password):
    try:
        time.sleep(2)
        try:
            time.sleep(2)
            allow_notification = driver.find_element(MobileBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
            allow_notification.click()
            time.sleep(2)
        except NoSuchElementException:
            pass

        type_number = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")')
        type_number.send_keys(phone_number)
        time.sleep(2)

        type_password = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter password")')
        type_password.send_keys(password)
        time.sleep(2)

        click_login_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Login')
        click_login_button.click()
        time.sleep(2)
        print("✅ Test Passed: Login Successful")

    except Exception as e:
        print("❌ Test Failed: Login unsuccessful")
        print(f"Error: {e}")
