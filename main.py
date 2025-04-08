from seleniumbase import Driver
from dotenv import load_dotenv
# initialize driver in GUI mode with UC enabled
driver = Driver(uc=True, headless=False)

# set the target URL
url = "https://www.scrapingcourse.com/cloudflare-challenge"

# open URL using UC mode with 6 second reconnect time
driver.uc_open_with_reconnect(url, reconnect_time=6)
