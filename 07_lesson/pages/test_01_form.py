import pytest
from selenium import webdriver
from main_page_01 import MainPage
from confirmation_page_01 import ConfirmationPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get
    ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()


def test_fill_form(driver):
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    main_page = MainPage(driver)
    main_page.fill_form(fields)
    main_page.click_submit()

    confirmation_page = ConfirmationPage(driver)

    zip_code_color = confirmation_page.get_zip_code_color()
    expected_zip_code_color = 'rgba(248, 215, 218, 1)'
    assert zip_code_color == expected_zip_code_color, (
        f"Expected Zip code background color: {expected_zip_code_color}, "
        f"but got: {zip_code_color}"
    )

    green_fields = ["first-name", "last-name", "address", "city", "e-mail",
                    "phone", "job-position", "company"]
    expected_green_color = 'rgba(209, 231, 221, 1)'

    for field_id in green_fields:
        field_color = confirmation_page.get_background_color(field_id)
        assert field_color == expected_green_color, (
            "Expected background color for {field_id}: "
            "{expected_green_color}, but got: {field_color}"
        )
