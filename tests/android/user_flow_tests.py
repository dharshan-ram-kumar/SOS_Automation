from utils.safe_run import safe_run

from tests.android.user.positive_cases.login import login
from tests.android.user.positive_cases.logout import logout
from tests.android.user.positive_cases.send_alert import send_alert
from tests.android.user.positive_cases.deactivate_alert import deactivate_alert
from tests.android.user.positive_cases.deactivate_medical_emergency_alert import deactivate_medical_emergency_alert
from tests.android.user.positive_cases.profile_image_update import profile_image_update
from tests.android.user.positive_cases.add_emergency_contact import add_emergency_contact
from tests.android.user.positive_cases.edit_emergency_contact import edit_emergency_contact
from tests.android.user.positive_cases.delete_emergency_contact import delete_emergency_contact
from tests.android.user.positive_cases.add_routes import add_routes
from tests.android.user.positive_cases.edit_routes import edit_routes
from tests.android.user.positive_cases.delete_route import delete_routes
from tests.android.user.positive_cases.add_frequent_location import add_frequent_location
from tests.android.user.positive_cases.edit_frequent_location import edit_frequent_location
from tests.android.user.positive_cases.delete_frequent_location import delete_frequent_location
from tests.android.user.positive_cases.view_privacy_policy import view_privacy_policy
from tests.android.user.positive_cases.view_safety_tips import view_safety
from tests.android.user.positive_cases.chat import chat
from tests.android.user.positive_cases.map import user_map
from tests.android.user.positive_cases.send_alert_safe_mode import send_alert_safe_mode
from tests.android.user.positive_cases.add_medical_emergency_contact import add_medical_emergency_contact
from tests.android.user.positive_cases.delete_medical_emergency_contact import delete_medical_emergency_contact
from tests.android.user.positive_cases.medical_alert_safe_mode import medical_alert_safe_mode
from tests.android.user.positive_cases.medical_emergency_alert import medical_emergency_alert

def run_user_flow(driver, phone_number, password):
    """Executes user test cases sequentially."""
    print("\n--- Executing User Test Flow ---\n")

    safe_run(login, driver, phone_number, password)
    safe_run(send_alert, driver)
    safe_run(deactivate_alert, driver)
    safe_run(medical_emergency_alert, driver)
    safe_run(deactivate_medical_emergency_alert, driver)
    safe_run(send_alert_safe_mode, driver)
    safe_run(medical_alert_safe_mode, driver)
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
    safe_run(user_map, driver)
    safe_run(chat, driver)
    safe_run(view_privacy_policy, driver)
    safe_run(logout, driver)
