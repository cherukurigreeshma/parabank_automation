import time
from pages.register_page import RegisterPage

def test_user_registration(driver):
    register_page = RegisterPage(driver)
    register_page.load()
    
    unique_user = f"user_{int(time.time())}"
    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Main St",
        "city": "Dallas",
        "state": "TX",
        "zip": "75001",
        "phone": "555-0199",
        "ssn": "000-00-0000",
        "username": unique_user,
        "password": "Password123"
    }
    
    register_page.register_user(user_data)
    assert "welcome" in driver.page_source.lower() or "created successfully" in driver.page_source.lower()