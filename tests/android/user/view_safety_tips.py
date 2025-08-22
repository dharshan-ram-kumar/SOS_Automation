from appium.webdriver.common.mobileby import MobileBy
from tests.android.user.menubar_access import menu_access

def view_safety(driver):
    try:
        menu_access(driver)

        view_safety_tips = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Safety Tips")')
        view_safety_tips.click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(5)'
        )
        print("✅ Test Passed: Safety tips displayed")

    except Exception as e:
        print("❌ Test Failed: Unable to display safety tips ")
        print(f"Error: {e}")
