from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def delete_routes(driver):
    try:
        click_delete = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'
        )
        click_delete.click()
        confirmation = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirmation.click()
        acknowledgement = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        acknowledgement.click()
        print("✅ Test Passed: Route deleted successful")

    except Exception as e:
        print("❌ Test Failed: Unable to delete route")
        print(f"Error: {e}")
