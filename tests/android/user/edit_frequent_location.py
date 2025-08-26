from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def edit_frequent_location(driver):
    try:
        navigate_routes = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("My Routes")')
        navigate_routes.click()
        click_location_tab = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Frequent Locations")')
        click_location_tab.click()
        edit_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        edit_location.click()
        pick_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        pick_location.click()
        my_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("🎯 My Location")')
        my_location.click()
        confirm_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Confirm")')
        confirm_location.click()

        click_save = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Update")')
        click_save.click()
        confirmation = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirmation.click()

        card = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(12)')
        if card:
            print("✅ Test Passed: Frequent location updated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to update frequent location")
        print(f"Error: {e}")
