import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from utils.wait_for_element import wait_for_element

def login(driver, phone_number, password):
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
        allow_location = driver.find_element(MobileBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        allow_location.click()
        print("✅ Test Passed: Login Successful")
        access1 = wait_for_element(driver,MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button',10)
        if access1:
            access1.click()
        access2 = wait_for_element(driver,MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        if access2:
            access2.click()
        access3 = wait_for_element(driver, MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_all_button')
        if access3:
            access3.click()
        access4 = wait_for_element(driver, MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button')
        if access4:
            access4.click()
        print("✅ Test Passed: All permission allowed")

    except Exception as e:
        print("❌ Test Failed: Login unsuccessful")
        print(f"Error: {e}")
