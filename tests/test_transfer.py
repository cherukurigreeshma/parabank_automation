import pytest
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

@pytest.mark.parametrize("amount,should_succeed", [
    ("100", True),
    ("0", False),
    ("-50", False),
])
def test_transfer_amounts(driver, amount, should_succeed):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("john", "demo")
    
    transfer_page = TransferPage(driver)
    transfer_page.load()
    transfer_page.transfer(amount)
    
    if should_succeed:
        assert "complete" in driver.page_source.lower()
    else:
        assert "error" in driver.page_source.lower() or "complete" not in driver.page_source.lower()