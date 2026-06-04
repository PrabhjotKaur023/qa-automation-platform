from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

CHROME_PATH = r"C:\chromedriver-win64\chromedriver.exe"


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)

    return driver