from selenium.common.exceptions import NoSuchWindowException, WebDriverException


def get_title(driver, query):
    try:
        # Check if the browser window is still open
        if not driver.window_handles:
            raise NoSuchWindowException("Browser window is closed")

        driver.get("https://musescore.com/sheetmusic?text=" + query)

        num = 1
        text = ""

        try:
            driver.sleep(2)
            text = driver.get_text(
                f"/html/body/div[1]/div[1]/section/section/main/div[2]/section/article[{num}]/div/div[2]/a/h2"
            )
            link = driver.get_attribute(
                f"/html/body/div[1]/div[1]/section/section/main/div[2]/section/article[{num}]/div/div[2]/a",
                "href",
            )
            while "Easy Piano" in text:
                num += 1
                text = driver.get_text(
                    f"/html/body/div[1]/div[1]/section/section/main/div[2]/section/article[{num}]/div/div[2]/a/h2"
                )
                link = driver.get_attribute(
                    f"/html/body/div[1]/div[1]/section/section/main/div[2]/section/article[{num}]/div/div[2]/a",
                    "href",
                )
        except WebDriverException as e:
            print(f"WebDriver error: {e}")
            text = "Error retrieving title"
            link = None
    except NoSuchWindowException as e:
        print(f"Error: {e}")
        text = "Browser window closed"
        link = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        text = "Error retrieving title"
        link = None

    return {"title": text, "link": link}
