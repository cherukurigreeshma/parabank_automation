import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    
    # Configure headless mode for CI environment
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)  # Increased from 10 to handle CI network lag
    driver.set_window_size(1920, 1080)
    return driver