import os
from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from tests.android.admin.active_alert import active_alert
from tests.android.admin.alert import admin_alert
from tests.android.admin.login import admin_login
from tests.android.admin.logout import admin_logout
from tests.android.primary_contact.alert import alert_pc
from tests.android.primary_contact.login import login_pc
from tests.android.primary_contact.logout import logout_pc
from tests.android.user.login import login
from tests.android.user.logout import logout
from tests.android.user.send_alert import send_alert
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
    # Send alert flow
    safe_run(login, driver, PHONE_NUMBER, PASSWORD)
    safe_run(send_alert, driver)
    print("✅ Test Passed: Alert sent from user side")
    safe_run(logout, driver)
    safe_run(login_pc, driver, PC_PHONE_NUMBER, PC_PASSWORD)
    safe_run(alert_pc, driver)
    safe_run(logout_pc, driver)
    safe_run(admin_login, driver, ADMIN_PHONE_NUMBER, ADMIN_PASSWORD)
    safe_run(active_alert, driver)
    safe_run(admin_logout, driver)

except Exception as e:
    print(f"Server error: {e}")

finally:
    print("\n--- Test Execution Completed ---")
    if driver:
        driver.quit()
