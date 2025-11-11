from appium.webdriver.common.appiumby import AppiumBy
from tests.android.user.positive_cases.menubar_access import menu_access


def view_safety(driver):
    try:
        menu_access(driver)

        view_safety_tips = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Safety Tips")'
        )
        view_safety_tips.click()
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(2)",
        )
        print("✅ Test Passed: Safety tips displayed")

    except Exception as e:
        print("❌ Test Failed: Unable to display safety tips ")
        print(f"Error: {e}")
