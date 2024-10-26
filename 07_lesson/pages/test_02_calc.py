import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get
    ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Открыть страницу калькулятора
    calculator_page = CalculatorPage(driver)

    # Ввести значение 45 в поле с локатором #delay
    calculator_page.set_delay("45")

    # Нажать на кнопки 7, +, 8, =
    buttons = ['7', '+', '8', '=']
    for button in buttons:
        calculator_page.click_button(button)

    # Ожидать появления результата
    calculator_page.wait_for_result("15")

    # Получаем текст результата
    result_text = calculator_page.get_result()
    print(f"Текущий текст результата: {result_text}")

    # Проверка, что результат действительно равен 15
    assert result_text == "15", "Ожидался результат 15, "
    "но получен: {result_text}"
