from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@type='submit']")
        self.site_name = (By.ID, "site-name")

    # Open login page
    def open(self):
        self.driver.get(f"{Config.BASE_URL}/admin")

    # Enter username
    def enter_username(self, username):
        element = self.wait.until(
            EC.presence_of_element_located(self.username_field)
        )
        element.clear()
        element.send_keys(username)

    # Enter password
    def enter_password(self, password):
        element = self.wait.until(
            EC.presence_of_element_located(self.password_field)
        )
        element.clear()
        element.send_keys(password)

    # Click login button
    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    # Validate login success
    def is_login_successful(self):
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.site_name)
            ).is_displayed()
        except:
            return False