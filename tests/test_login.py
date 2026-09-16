import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    d = get_driver()
    yield d
    d.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("john", "demo")
    assert "accounts" in driver.current_url.lower() or "overview" in driver.page_source.lower()

def test_invalid_login_shows_error(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wronguser", "wrongpass")
    assert "error" in driver.page_source.lower()