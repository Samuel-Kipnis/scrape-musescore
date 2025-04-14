import json
import time
import os
from download import download


def mass_download(driver, pieces):
    for piece in pieces:
        if piece["status"] == "✅ Success":
            print(f"⬇️ Attempting to download: {piece['title']} ({piece['query']})")
            try:
                download(driver, piece["link"])
                print(f"✅ Successfully downloaded: {piece['title']}")
            except Exception as e:
                print(f"❌ Failed to download '{piece['title']}': {e}")

    time.sleep(10)  # Wait for downloads to complete
    print("✅ All downloads attempted.")


if __name__ == "__main__":
    from login import login  # Assuming login is in login.py
    import undetected_chromedriver as uc

    folder_path = "./pkl_cookies"  # Path to your cookies folder
    cookie_files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    json_path = "finalist_sheet_music_results.json"  # Make sure this JSON exists

    data = []
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    successful_data = [item for item in data if item["status"] != "❌ Failed"]

    def split_into_chunks(lst, chunk_size=20):
        return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]

    # Example usage
    chunks = split_into_chunks(successful_data, 20)

    # Setup driver
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    for i, chunk in enumerate(chunks):
        login(driver, cookie_files[i])
        mass_download(driver, chunk)
        time.sleep(1)

    # login(driver)  # Log in to MuseScore

    # json_path = "sheet_music_results.json"  # Make sure this JSON exists
    # download_from_json(driver, json_path)

    # driver.quit()
    # print("✅ All downloads attempted.")
