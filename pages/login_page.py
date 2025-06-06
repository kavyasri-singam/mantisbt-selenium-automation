from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "input[type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def submit_username(self):
        self.driver.find_element(*self.login_button).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit_password(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.submit_username()
        self.enter_password(password)
        self.submit_password()
