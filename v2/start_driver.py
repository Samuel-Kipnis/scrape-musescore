import undetected_chromedriver as uc


def start_driver():
    # Set up undetected Chrome driver
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument(
        "--headless"
    )  # Run headless (without opening a visible browser)
    options.add_argument("--disable-software-rasterizer")

    driver = uc.Chrome(options=options)
    return driver
