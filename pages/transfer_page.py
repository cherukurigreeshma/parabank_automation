from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased timeout for CI
        self.amount_input = (By.ID, "amount")
        self.transfer_btn = (By.XPATH, "//input[@value='Transfer']")

    def load(self):
        self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
        # Wait until body is present to confirm page navigation completed
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def transfer(self, amount):
        # Wait explicitly for the amount field to become clickable
        amount_field = self.wait.until(
            EC.element_to_be_clickable(self.amount_input)
        )
        amount_field.clear()
        amount_field.send_keys(str(amount))
        
        # Click transfer button
        self.wait.until(
            EC.element_to_be_clickable(self.transfer_btn)
        ).click()