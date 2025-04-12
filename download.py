import time


def download(driver):
    driver.click("/html/body/div/div[1]/section/aside/div[1]/div/section/button[1]")
    time.sleep(0.5)
    driver.click("/html/body/article/section/section/div/section/section/div[3]")
