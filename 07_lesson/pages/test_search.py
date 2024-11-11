import pytest
from selenium import webdriver
from MainPageGoogle import MainPageGoogle


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()


def test_search(driver):
    page = MainPageGoogle(driver)
    page.search_for("Selenium Python")
    results = page.get_search_results()

    assert len(results) > 0, "Результаты поиска не найдены."
