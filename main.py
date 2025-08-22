import os
from appium import webdriver
from dotenv import load_dotenv
from tests.android.user.add_emergency_contact import add_emergency_contact
from tests.android.user.delete_emergency_contact import delete_emergency_contact
from tests.android.user.edit_emergency_contact import edit_emergency_contact
from tests.android.user.login import login
from tests.android.user.profile_image_update import profile
from tests.android.user.send_alert import send_alert
from tests.android.user.view_safety_tips import view_safety

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
PASSWORD = os.getenv("PASSWORD")

desired_caps = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:appActivity": "com.tringapps.womensos.MainActivity",
    "appium:appPackage": "com.tringapps.womensos",
    "app": os.path.abspath("./build/WomenSOS.apk"),
    # "noReset": True, #Clear app data and cache
    # "fullReset": True #Reinstall app each time
}

driver = None
try:
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    login(driver, PHONE_NUMBER, PASSWORD)
    profile(driver)
    view_safety(driver)
    add_emergency_contact(driver)
    edit_emergency_contact(driver)
    delete_emergency_contact(driver)
    send_alert(driver)

finally:
    print("Test Completed")
