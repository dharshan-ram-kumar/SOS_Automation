import os
from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from tests.android.admin.admin_alert import admin_alert
from tests.android.admin.admin_chat import admin_chat
from tests.android.admin.admin_login import admin_login
from tests.android.admin.admin_logout import admin_logout
from tests.android.admin.admin_map import admin_map

from tests.android.user.positive_cases.deactivate_alert import deactivate_alert
from tests.android.user.positive_cases.deactivate_medical_emergency_alert import deactivate_medical_emergency_alert
from tests.android.user.positive_cases.add_emergency_contact import add_emergency_contact
from tests.android.user.positive_cases.add_frequent_location import add_frequent_location
from tests.android.user.positive_cases.add_medical_emergency_contact import add_medical_emergency_contact
from tests.android.user.positive_cases.add_routes import add_routes
from tests.android.user.positive_cases.delete_emergency_contact import delete_emergency_contact
from tests.android.user.positive_cases.delete_frequent_location import delete_frequent_location
from tests.android.user.positive_cases.delete_medical_emergency_contact import delete_medical_emergency_contact
from tests.android.user.positive_cases.delete_route import delete_routes
from tests.android.user.positive_cases.edit_emergency_contact import edit_emergency_contact
from tests.android.user.positive_cases.edit_frequent_location import edit_frequent_location
from tests.android.user.positive_cases.edit_routes import edit_routes
from tests.android.user.positive_cases.login import login
from tests.android.user.positive_cases.logout import logout
from tests.android.user.positive_cases.map import user_map
from tests.android.user.positive_cases.medical_alert_safe_mode import send_medical_alert_safe_mode
from tests.android.user.positive_cases.medical_emergency_alert import send_medical_emergency_alert
from tests.android.user.positive_cases.profile_image_update import profile_image_update
from tests.android.user.positive_cases.send_alert import send_alert
from tests.android.user.positive_cases.view_privacy_policy import view_privacy_policy
from tests.android.user.positive_cases.view_safety_tips import view_safety
from tests.android.user.positive_cases.send_alert_safe_mode import send_alert_safe_mode
from tests.android.user.positive_cases.chat import chat

from utils.safe_run import safe_run

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
PASSWORD = os.getenv("PASSWORD")
ADMIN_PHONE_NUMBER = os.getenv("ADMIN_PHONE_NUMBER")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
EMULATOR_NAME = os.getenv("EMULATOR_NAME","emulator-5554")
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL","http://127.0.0.1:4723")
APP_PATH = os.path.abspath("build/WomenSOS.apk")

options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("deviceName", EMULATOR_NAME)
options.set_capability("appPackage", "com.tringapps.womensos")
options.set_capability("appActivity", "com.tringapps.womensos.MainActivity")
options.set_capability("app", APP_PATH)

driver = None

try:
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    print("\n--- Test Execution Started ---\n")

    # User flow
    safe_run(login, driver, PHONE_NUMBER, PASSWORD)
    safe_run(send_alert, driver)
    safe_run(deactivate_alert, driver)
    safe_run(send_medical_emergency_alert, driver)
    safe_run(deactivate_medical_emergency_alert,driver)
    safe_run(send_alert_safe_mode, driver)
    safe_run(send_medical_alert_safe_mode, driver)
    safe_run(profile_image_update, driver)
    safe_run(view_safety, driver)
    safe_run(add_emergency_contact, driver)
    safe_run(edit_emergency_contact, driver)
    safe_run(delete_emergency_contact, driver)
    safe_run(add_medical_emergency_contact, driver)
    # safe_run(edit_medical_emergency_contact,driver) #error
    safe_run(delete_medical_emergency_contact, driver)
    safe_run(add_routes, driver)
    safe_run(edit_routes, driver)
    safe_run(delete_routes, driver)
    safe_run(add_frequent_location, driver)
    safe_run(edit_frequent_location, driver)
    safe_run(delete_frequent_location, driver)
    safe_run(user_map,driver)
    safe_run(chat, driver)
    safe_run(view_privacy_policy, driver)
    safe_run(logout, driver)

    # Admin flow
    safe_run(admin_login, driver, ADMIN_PHONE_NUMBER, ADMIN_PASSWORD)
    safe_run(admin_alert, driver)
    safe_run(admin_map, driver)
    safe_run(admin_chat, driver)
    safe_run(admin_logout, driver)

except Exception as e:
    print(f"Server error: {e}")

finally:
    print("\n--- Test Execution Completed ---")
    if driver:
        driver.quit()
