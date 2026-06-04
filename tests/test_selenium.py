from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_open_browser():
    service = Service(r"C:\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://google.com")

    assert "Google" in driver.title

    driver.quit()