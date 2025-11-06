import os
from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from tests.android.admin.alert import admin_alert
from tests.android.admin.chat import admin_chat
from tests.android.admin.login import admin_login
from tests.android.admin.logout import admin_logout
from tests.android.admin.map import admin_map
from tests.android.user import deactivate_medical_emergency_alert
from tests.android.user.add_emergency_contact import add_emergency_contact
from tests.android.user.add_frequent_location import add_frequent_location
from tests.android.user.add_medical_emergency_contact import add_medical_emergency_contact
from tests.android.user.add_routes import add_routes
from tests.android.user.deactivate_alert import deactivate_alert
from tests.android.user.delete_emergency_contact import delete_emergency_contact
from tests.android.user.delete_frequent_location import delete_frequent_location
from tests.android.user.delete_medical_emergency_contact import delete_medical_emergency_contact
from tests.android.user.delete_route import delete_routes
from tests.android.user.edit_emergency_contact import edit_emergency_contact
from tests.android.user.edit_frequent_location import edit_frequent_location
from tests.android.user.edit_medical_emergency_contact import edit_medical_emergency_contact
from tests.android.user.edit_routes import edit_routes
from tests.android.user.login import login
from tests.android.user.logout import logout
from tests.android.user.medical_alert_safe_mode import send_medical_alert_safe_mode
from tests.android.user.medical_emergency_alert import send_medical_emergency_alert
from tests.android.user.profile_image_update import profile_image_update
from tests.android.user.send_alert import send_alert
from tests.android.user.view_privacy_policy import view_privacy_policy
from tests.android.user.view_safety_tips import view_safety
from tests.android.user.send_alert_safe_mode import send_alert_safe_mode
from tests.android.user.chat import chat
from utils.safe_run import safe_run

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
PASSWORD = os.getenv("PASSWORD")
ADMIN_PHONE_NUMBER = os.getenv("ADMIN_PHONE_NUMBER")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("deviceName", "emulator-5554")
options.set_capability("appPackage", "com.tringapps.womensos")
options.set_capability("appActivity", "com.tringapps.womensos.MainActivity")
options.set_capability("app", os.path.abspath("build/WomenSOS1.apk"))

driver = None

try:
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
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
    # safe_run(edit_emergency_contact, driver)
    safe_run(delete_emergency_contact, driver)
    safe_run(add_medical_emergency_contact, driver)
    safe_run(edit_medical_emergency_contact,driver)
    safe_run(delete_medical_emergency_contact, driver)
    safe_run(add_routes, driver)
    safe_run(edit_routes, driver)
    safe_run(delete_routes, driver)
    safe_run(add_frequent_location, driver)
    safe_run(edit_frequent_location, driver)
    safe_run(delete_frequent_location, driver)
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
