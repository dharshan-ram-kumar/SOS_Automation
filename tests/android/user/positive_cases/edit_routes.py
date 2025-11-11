import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.wait_for_element import wait_for_element


def edit_routes(driver):
    try:
        navigate_routes = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("My Routes")'
        )
        navigate_routes.click()
        click_route_tab = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("My Trips")'
        )
        click_route_tab.click()
        click_edit = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'
        )
        click_edit.click()

        time.sleep(2)
        start_time = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("09:30")'
        )
        start_time.clear()
        start_time = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Start Time (e.g. 09:30)")',
        )
        start_time.send_keys("09:00")
        end_time = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("18:45")'
        )
        end_time.clear()
        end_time = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("End Time (e.g. 18:45)")',
        )
        end_time.send_keys("10:35")
        click_save = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Update")'
        )
        click_save.click()
        confirmation = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        confirmation.click()

        card = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup").instance(12)',
        )
        if card:
            print("✅ Test Passed: Route updated successful")

    except Exception as e:
        print("❌ Test Failed: Unable to update route")
        print(f"Error: {e}")
