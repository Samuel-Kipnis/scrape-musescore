import pickle
import time

MUSESCORE_URL = "https://musescore.com"


def login(driver, cookies_file):
    """Load cookies and log in to MuseScore."""
    driver.get(MUSESCORE_URL)
    time.sleep(2)  # Ensure page is fully loaded for domain context

    with open(f"./pkl_cookies/{cookies_file}", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(2)
    print("✅ You are now logged in using saved session.")
