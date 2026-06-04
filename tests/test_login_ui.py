from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_admin_login():
    service = Service(r"C:\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("http://127.0.0.1:8000/admin")

    time.sleep(2)

    # Enter username
    driver.find_element(By.ID, "id_username").send_keys("admin")

    # Enter password
    driver.find_element(By.ID, "id_password").send_keys("admin@2003K")

    # Click login
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(2)

    # Validate login success
    assert "Site administration" in driver.page_source

    driver.quit()