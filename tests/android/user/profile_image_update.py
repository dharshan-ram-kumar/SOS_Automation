from appium.webdriver.common.appiumby import AppiumBy
from tests.android.user.menubar_access import menu_access
from utils.wait_for_element import wait_for_element


def profile(driver):
    try:
        menu_access(driver)

        click_profile = wait_for_element(
            driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Profile")'
        )
        click_profile.click()

        change_profile = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("").instance(0)',
            timeout=5,
        )
        if change_profile:
            change_profile.click()

        change_existing_profile = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Change Profile Image")',
            timeout=5,
        )
        if change_existing_profile:
            change_existing_profile.click()

        choose_image = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.RelativeLayout")',
        )
        choose_image.click()

        choose_image1 = wait_for_element(
            driver,
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Photo taken on Aug 19, 2025 4:30 PM")',
        )
        choose_image1.click()

        success_message = wait_for_element(driver, AppiumBy.ID, "android:id/button1")
        success_message.click()
        print("✅ Test Passed: Profile image update successful")

    except Exception as e:
        print("❌ Test Failed: Profile image update unsuccessful")
        print(f"Error: {e}")
