from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
        # Locators
        self.amount_input = (By.ID, "amount")
        self.from_account_select = (By.ID, "fromAccountId")
        self.to_account_select = (By.ID, "toAccountId")
        self.transfer_btn = (By.XPATH, "//input[@value='Transfer']")
        self.result_message = (By.XPATH, "//div[@id='showResult'] | //span[@class='error']")

    def transfer_funds(self, amount, from_index=0, to_index=0):
        # Wait for the amount field to be visible
        self.wait.until(EC.visibility_of_element_located(self.amount_input)).send_keys(str(amount))
        
        # Wait until dropdown options are populated (more than 0 options)
        self.wait.until(lambda d: len(Select(d.find_element(*self.from_account_select)).options) > 0)
        
        from_dropdown = Select(self.driver.find_element(*self.from_account_select))
        to_dropdown = Select(self.driver.find_element(*self.to_account_select))
        
        from_dropdown.select_by_index(from_index)
        to_dropdown.select_by_index(to_index)
        
        # Click transfer
        self.wait.until(EC.element_to_be_clickable(self.transfer_btn)).click()

    def get_result_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.result_message)).text