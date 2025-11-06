# Function to avoid test execution crashes
def safe_run(test_func, *args):
    try:
        print(f"Running test: {test_func.__name__}")
        test_func(*args)
    except Exception as e:
        print(f"❌ Failed: {test_func.__name__} - {e}")