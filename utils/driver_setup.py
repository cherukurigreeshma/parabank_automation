import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    
    # Enable headless mode if running in CI environment (GitHub Actions)
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver