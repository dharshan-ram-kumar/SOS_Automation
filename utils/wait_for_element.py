import time

def wait_for_element(driver, by, value, timeout=10):
    """Custom wait using only Appium find_elements"""
    end_time = time.time() + timeout
    while time.time() < end_time:
        elements = driver.find_elements(by, value)
        if elements:
            return elements[0]
        time.sleep(0.5)  # retry every 0.5 sec
    return None