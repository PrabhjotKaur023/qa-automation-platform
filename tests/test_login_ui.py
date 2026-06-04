from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_django_admin_login():
    service = Service(r"C:\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        login_page = LoginPage(driver)

        login_page.open_login_page()
        login_page.login("admin", "admin@2003K")

        # Wait for successful login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Validate login success
        assert "logout" in driver.page_source.lower()

    finally:
        driver.quit()