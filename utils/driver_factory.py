from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverFactory:

    @staticmethod
    def get_driver():
        service = Service()  # ChromeDriver should be in PATH now
        options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver