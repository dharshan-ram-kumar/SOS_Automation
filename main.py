import os
from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from tests.android.user_flow_tests import run_user_flow
from tests.android.admin_flow_tests import run_admin_flow
from tests.android.parallel_test_flow import run_parallel_test_flow

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
PASSWORD = os.getenv("PASSWORD")
PC_PHONE_NUMBER = os.getenv("PC_PHONE_NUMBER")
PC_PASSWORD = os.getenv("PC_PASSWORD")
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
    print("--- Test Execution Started ---")

    # User flow
    run_user_flow(driver, PHONE_NUMBER, PASSWORD)

    # Admin flow
    run_admin_flow(driver, ADMIN_PHONE_NUMBER, ADMIN_PASSWORD)

    # Parallel flow
    run_parallel_test_flow(driver, PHONE_NUMBER, PASSWORD, ADMIN_PHONE_NUMBER, ADMIN_PASSWORD,PC_PHONE_NUMBER, PC_PASSWORD)

except Exception as e:
    print(f"Server Error: {e}")

finally:
    print("--- Test Execution Completed ---")
    if driver:
        driver.quit()
