import time


def search(driver, query):
    driver.get("https://musescore.com/sheetmusic?text=" + query)

    # turn on filter
    driver.click(
        "body > div.js-page.react-container > div.b1GqE > section > section > aside > div:nth-child(1) > div:nth-child(3) > div.PI5Hd.g1QZl > label:nth-child(2) > div > div > div.C4LKv.DIiWA"
    )

    time.sleep(1)
    driver.click(
        "body > div.js-page.react-container > div.b1GqE > section > section > main > div > section > article:nth-child(2) > div.dhaTG.J5IQp > div.ksWwy > a > div"
    )
