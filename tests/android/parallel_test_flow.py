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

def run_parallel_test_flow(driver,phone_number, password,admin_phone_number,admin_password,pc_phone_number,pc_password):
    """Execute parallel flow test cases sequentially."""
    print("\n--- Executing Parallel Test Flow Started ---\n")

    # Send alert from user login
    safe_run(login, driver, phone_number, password)
    safe_run(send_alert, driver)
    print("✅ Test Passed: Alert sent from user side")
    safe_run(logout, driver)

    # Verify alert in primary contact login
    safe_run(pc_login, driver, pc_phone_number, pc_password)
    safe_run(pc_verify_alert, driver)
    safe_run(pc_logout, driver)

    # Verify alert in admin login
    safe_run(admin_login, driver, admin_phone_number, admin_password)
    safe_run(admin_verify_alert, driver)
    safe_run(admin_logout, driver)

