from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    logout_link = (By.LINK_TEXT, "Log out")

    # Actions
    def is_dashboard_loaded(self):
        return "site administration" in self.driver.page_source.lower()

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()