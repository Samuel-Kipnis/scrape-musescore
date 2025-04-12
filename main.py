from start_driver import start_driver
from search import search
from download import download
from login import login
from get_title import get_title
import time
import json
import pandas as pd


def main():
    df = pd.read_csv("cleanlist.csv")
    df["Composite"] = df["Composer"] + " " + df["Piece"]

    driver = start_driver()
    login(driver)

    # loop through list of composers and pieces
    titles = {}
    for title in df["Composite"][:5]:
        titles[title] = get_title(driver, title)
        # search(driver, title)
        # download(driver)

    with open("titles.json", "w") as json_file:
        json.dump(titles, json_file, indent=4)

    time.sleep(100000000)


if __name__ == "__main__":
    main()
