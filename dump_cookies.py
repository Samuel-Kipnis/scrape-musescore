import undetected_chromedriver as uc
import pickle
import time
import sys

print(sys.argv[1])

# Start browser
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

# Go to MuseScore login page
driver.get("https://musescore.com/user/login")

print("🛑 Please log in manually (solve CAPTCHA if shown).")
input("✅ Press ENTER after you have successfully logged in...")

# Save cookies
with open(f"./pkl_cookies/musescore_cookies_{sys.argv[1]}@mail.com.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Session cookies saved!")
driver.quit()
