from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://parabank.parasoft.com/parabank/transfer.htm"
        self.amount_input = (By.ID, "amount")
        self.transfer_button = (By.XPATH, "//input[@value='Transfer']")

    def load(self):
        self.driver.get(self.url)

    def transfer(self, amount):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.amount_input)).send_keys(amount)
        self.driver.find_element(*self.transfer_button).click()