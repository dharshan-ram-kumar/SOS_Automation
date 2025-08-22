from appium.webdriver.common.mobileby import MobileBy

def my_routes(driver):
    try:
        navigate_routes = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("My Routes")')
        navigate_routes.click()
        add_trip = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Add Trip")')
        add_trip.click()
        pick_from_location = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)')
        pick_from_location.click()
        search_from_location = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Search location...")')
        search_from_location.send_keys("Chennai")
        select_from_location = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)')
        select_from_location.click()
        confirm_from_location = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Confirm")')
        confirm_from_location.click()


    except Exception as e:
        print("❌ Test Failed: Unable to send alert")
        print(f"Error: {e}")
