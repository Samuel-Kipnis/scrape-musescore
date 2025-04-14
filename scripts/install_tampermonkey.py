import time


def install_tampermonkey(driver):
    # https://www.tampermonkey.net/script_installation.php#url=https://github.com/LibreScore/dl-librescore/releases/latest/download/dl-librescore.user.js
    # driver.get(
    #     "https://www.tampermonkey.net/script_installation.php#url=https://github.com/LibreScore/dl-librescore/releases/latest/download/dl-librescore.user.js"
    # )
    # driver.get("chrome-extension://dhdgffkkebhmkfjojejmpbldmpobfkfo/options.html")
    time.sleep(100)  # Wait for the page to load


if __name__ == "__main__":
    # from login import login  # Assuming login is in login.py
    import undetected_chromedriver as uc

    # Setup driver
    options = uc.ChromeOptions()
    options.add_extension(
        "C:/Coding/scrape-musescore/tampermonkey.crx"
    )  # Path to your Tampermonkey extension
    driver = uc.Chrome(options=options)

    # login(driver)  # Log in to MuseScore

    install_tampermonkey(driver)  # Install Tampermonkey script
