def test_open_browser(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title