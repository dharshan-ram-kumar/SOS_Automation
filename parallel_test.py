import os
from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from tests.android.admin.admin_login import admin_login
from tests.android.admin.admin_verify_alert import admin_verify_alert
from tests.android.admin.admin_logout import admin_logout

from tests.android.primary_contact.pc_verify_alert import pc_verify_alert
from tests.android.primary_contact.pc_login import pc_login
from tests.android.primary_contact.pc_logout import pc_logout

from tests.android.user.positive_cases.login import login
from tests.android.user.positive_cases.logout import logout
from tests.android.user.positive_cases.send_alert import send_alert

from utils.safe_run import safe_run

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
PASSWORD = os.getenv("PASSWORD")
ADMIN_PHONE_NUMBER = os.getenv("ADMIN_PHONE_NUMBER")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
PC_PHONE_NUMBER = os.getenv("PC_PHONE_NUMBER")
PC_PASSWORD = os.getenv("PC_PASSWORD")
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

    # Send alert from user login
    safe_run(login, driver, PHONE_NUMBER, PASSWORD)
    safe_run(send_alert, driver)
    print("✅ Test Passed: Alert sent from user side")
    safe_run(logout, driver)

    # Verify alert in primary contact login
    safe_run(pc_login, driver, PC_PHONE_NUMBER, PC_PASSWORD)
    safe_run(pc_verify_alert, driver)
    safe_run(pc_logout, driver)

    # Verify alert in admin login
    safe_run(admin_login, driver, ADMIN_PHONE_NUMBER, ADMIN_PASSWORD)
    safe_run(admin_verify_alert, driver)
    safe_run(admin_logout, driver)

except Exception as e:
    print(f"Server error: {e}")

finally:
    print("\n--- Test Execution Completed ---")
    if driver:
        driver.quit()
