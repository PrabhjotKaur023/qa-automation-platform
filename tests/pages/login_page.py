from selenium.webdriver.common.by import By
from utils.config_reader import load_config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//input[@type='submit']")

    def open(self, env="dev"):
        config = load_config(env)
        self.driver.get(config["base_url"])

    def login(self, username, password):

        self.driver.find_element(
            *self.username
        ).send_keys(username)

        self.driver.find_element(
            *self.password
        ).send_keys(password)

        self.driver.find_element(
            *self.login_button
        ).click()