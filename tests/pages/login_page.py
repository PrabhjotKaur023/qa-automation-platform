from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//input[@type='submit']")

    def open(self):
        self.driver.get("http://127.0.0.1:8000/admin/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()