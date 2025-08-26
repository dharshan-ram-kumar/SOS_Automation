from appium.webdriver.common.mobileby import MobileBy
from utils.wait_for_element import wait_for_element

def add_routes(driver):
    try:
        navigate_routes =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("My Routes")')
        navigate_routes.click()
        click_route_tab = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("My Trips")')
        click_route_tab.click()
        add_trip =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Add Trip")')
        add_trip.click()
        pick_from_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)')
        pick_from_location.click()
        search_from_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Search location...")')
        search_from_location.send_keys("Chennai")
        select_from_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)',10)
        select_from_location.click()
        confirm_from_location = wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Confirm")')
        confirm_from_location.click()

        pick_to_location =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(1)')
        pick_to_location.click()
        search_to_location =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Search location...")')
        search_to_location.send_keys("Chennai")
        select_to_location =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(1)',10)
        select_to_location.click()
        confirm_to_location =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Confirm")')
        confirm_to_location.click()

        start_time =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Start Time (e.g. 09:30)")')
        start_time.send_keys("09:30")
        end_time =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("End Time (e.g. 18:45)")')
        end_time.send_keys("18:45")
        click_save =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Save")')
        click_save.click()
        confirmation = wait_for_element(driver,MobileBy.ID,'android:id/button1')
        confirmation.click()

        card =wait_for_element(driver,MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(12)')
        if card:
            print("✅ Test Passed: Route added successful")

    except Exception as e:
        print("❌ Test Failed: Unable to add route")
        print(f"Error: {e}")
