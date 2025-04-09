from start_driver import start_driver
from download_score import download_score
from login import login
import time


def main():
    driver = start_driver()
    login(driver)

    url = "https://musescore.com/user/6662591/scores/4383881"
    download_score(driver, url)
    time.sleep(50)  # Wait for the download to finish


if __name__ == "__main__":
    main()
