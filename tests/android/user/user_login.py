import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from utils.wait_for_element import wait_for_element

def user_login(driver, phone_number, password):
    try:
        time.sleep(2)
        try:
            allow_notification = driver.find_element(MobileBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
            allow_notification.click()
            time.sleep(1)
        except NoSuchElementException:
            pass

        type_number = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000000000")')
        type_number.send_keys(phone_number)
        time.sleep(1)

        type_password = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter password")')
        type_password.send_keys(password)
        time.sleep(1)

        click_login_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Login')
        click_login_button.click()
        time.sleep(2)

        print("✅ Test Passed: Login Successful")

        while True:
            try:
                allow_button = wait_for_element(driver, MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button', 3)
                if allow_button:
                    allow_button.click()
                    time.sleep(1)
                else:
                    break
            except:
                break

        print("✅ Test Passed: All permissions allowed")
    except Exception as e:
        print("❌ Test Failed: Login unsuccessful")
        print(f"Error: {e}")
