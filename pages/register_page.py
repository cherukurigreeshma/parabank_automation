from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://parabank.parasoft.com/parabank/register.htm"
        self.first_name = (By.ID, "customer.firstName")
        self.last_name = (By.ID, "customer.lastName")
        self.address = (By.ID, "customer.address.street")
        self.city = (By.ID, "customer.address.city")
        self.state = (By.ID, "customer.address.state")
        self.zip_code = (By.ID, "customer.address.zipCode")
        self.phone = (By.ID, "customer.phoneNumber")
        self.ssn = (By.ID, "customer.ssn")
        self.username = (By.ID, "customer.username")
        self.password = (By.ID, "customer.password")
        self.confirm_password = (By.ID, "repeatedPassword")
        self.register_button = (By.XPATH, "//input[@value='Register']")

    def load(self):
        self.driver.get(self.url)

    def register_user(self, user_data):
        self.driver.find_element(*self.first_name).send_keys(user_data["first_name"])
        self.driver.find_element(*self.last_name).send_keys(user_data["last_name"])
        self.driver.find_element(*self.address).send_keys(user_data["address"])
        self.driver.find_element(*self.city).send_keys(user_data["city"])
        self.driver.find_element(*self.state).send_keys(user_data["state"])
        self.driver.find_element(*self.zip_code).send_keys(user_data["zip"])
        self.driver.find_element(*self.phone).send_keys(user_data["phone"])
        self.driver.find_element(*self.ssn).send_keys(user_data["ssn"])
        self.driver.find_element(*self.username).send_keys(user_data["username"])
        self.driver.find_element(*self.password).send_keys(user_data["password"])
        self.driver.find_element(*self.confirm_password).send_keys(user_data["password"])
        self.driver.find_element(*self.register_button).click()