from utils.safe_run import safe_run
from tests.android.admin.admin_login import admin_login
from tests.android.admin.admin_logout import admin_logout
from tests.android.admin.admin_alert import admin_alert
from tests.android.admin.admin_chat import admin_chat
from tests.android.admin.admin_map import admin_map


def run_admin_flow(driver, admin_phone_number, admin_password):
    """Executes admin test cases sequentially."""
    print("\n--- Executing Admin Test Flow ---\n")

    safe_run(admin_login, driver, admin_phone_number, admin_password)
    safe_run(admin_alert, driver)
    safe_run(admin_map, driver)
    safe_run(admin_chat, driver)
    safe_run(admin_logout, driver)
