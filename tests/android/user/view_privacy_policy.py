from appium.webdriver.common.mobileby import MobileBy
from tests.android.user.menubar_access import menu_access

def view_privacy_policy(driver):
    try:
        menu_access(driver)

        click_privacy_policy = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Privacy Policy")')
        click_privacy_policy.click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(3)'
        )
        print("✅ Test Passed: Privacy policy displayed")

    except Exception as e:
        print("❌ Test Failed: Unable to display privacy policy")
        print(f"Error: {e}")
