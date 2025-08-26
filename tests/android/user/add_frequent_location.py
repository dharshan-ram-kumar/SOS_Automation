from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def add_frequent_location(driver):
    try:
        navigate_routes = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("My Routes")')
        navigate_routes.click()
        click_location_tab = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Frequent Locations")')
        click_location_tab.click()
        add_trip = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Add Location")')
        add_trip.click()
        pick_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        pick_location.click()
        search_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Search location...")')
        search_location.send_keys("Chennai")
        select_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)',10)
        select_location.click()
        confirm_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Confirm")')
        confirm_location.click()

        start_time = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Start Time (e.g. 09:30)")')
        start_time.send_keys("09:30")
        end_time = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("End Time (e.g. 18:45)")')
        end_time.send_keys("18:45")
        click_save = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Save")')
        click_save.click()
        confirmation = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirmation.click()

        card = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(12)')
        if card:
            print("✅ Test Passed: Frequent location added successful")

    except Exception as e:
        print("❌ Test Failed: Unable to add frequent location")
        print(f"Error: {e}")
