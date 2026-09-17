import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.amount_input = (By.ID, "amount")
        self.from_account_select = (By.ID, "fromAccountId")
        self.to_account_select = (By.ID, "toAccountId")
        self.transfer_btn = (By.XPATH, "//input[@value='Transfer']")
        self.result_container = (By.ID, "showResult")
        self.error_message = (By.CLASS_NAME, "error")

    def transfer_funds(self, amount, from_index=0, to_index=0):
        # 1. Wait for amount field to be visible
        amount_element = self.wait.until(EC.visibility_of_element_located(self.amount_input))
        amount_element.clear()
        amount_element.send_keys(str(amount))
        
        # 2. Wait until AJAX populates the dropdowns (at least 1 option must exist)
        self.wait.until(
            lambda d: len(Select(d.find_element(*self.from_account_select)).options) > 0
        )
        
        # Select options
        from_dropdown = Select(self.driver.find_element(*self.from_account_select))
        to_dropdown = Select(self.driver.find_element(*self.to_account_select))
        
        from_dropdown.select_by_index(from_index)
        to_dropdown.select_by_index(to_index)
        
        # Brief pause to ensure DOM state stabilizes before form submit
        time.sleep(1)
        
        # 3. Click transfer
        self.wait.until(EC.element_to_be_clickable(self.transfer_btn)).click()

    def get_result_text(self):
        # Wait for either result container or error message to appear
        element = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='showResult'] | //span[@class='error'] | //p[@class='error']")
            )
        )
        return element.text