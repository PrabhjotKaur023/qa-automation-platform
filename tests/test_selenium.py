def test_open_browser(driver):

    driver.get("http://127.0.0.1:8000/admin/")

    assert "Django" in driver.title