import os
from appium import webdriver
from dotenv import load_dotenv
from tests.android.admin.alert import admin_alert
from tests.android.admin.chat import admin_chat
from tests.android.admin.login import admin_login
from tests.android.admin.logout import admin_logout
from tests.android.admin.map import admin_map
from tests.android.user.add_emergency_contact import add_emergency_contact
from tests.android.user.add_frequent_location import add_frequent_location
from tests.android.user.add_routes import add_routes
from tests.android.user.deactivate_alert import deactivate_alert
from tests.android.user.delete_emergency_contact import delete_emergency_contact
from tests.android.user.delete_frequent_location import delete_frequent_location
from tests.android.user.delete_route import delete_routes
from tests.android.user.edit_emergency_contact import edit_emergency_contact
from tests.android.user.edit_frequent_location import edit_frequent_location
from tests.android.user.edit_routes import edit_routes
from tests.android.user.login import login
from tests.android.user.logout import logout
from tests.android.user.profile_image_update import profile
from tests.android.user.send_alert import send_alert
from tests.android.user.view_privacy_policy import view_privacy_policy
from tests.android.user.view_safety_tips import view_safety
from tests.android.user.allow_video import allow_video
from tests.android.user.chat import chat

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
PASSWORD = os.getenv("PASSWORD")
ADMIN_PHONE_NUMBER = os.getenv("ADMIN_PHONE_NUMBER")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

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
    print("Test Started")
    login(driver, PHONE_NUMBER, PASSWORD)
    profile(driver)
    view_safety(driver)
    # view_privacy_policy(driver)
    add_emergency_contact(driver)
    edit_emergency_contact(driver)
    delete_emergency_contact(driver)
    send_alert(driver)
    deactivate_alert(driver)
    add_routes(driver)
    edit_routes(driver)
    delete_routes(driver)
    add_frequent_location(driver)
    edit_frequent_location(driver)
    delete_frequent_location(driver)
    # allow_video(driver)
    chat(driver)
    logout(driver)

    admin_login(driver, ADMIN_PHONE_NUMBER, ADMIN_PASSWORD)
    # admin_alert(driver)
    admin_map(driver)
    admin_chat(driver)
    admin_logout(driver)

finally:
    print("Test Completed")
