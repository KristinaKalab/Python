import pytest
from selenium import webdriver
from calcpage import SlowCalculatorPage  # Import the class

@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()


def test_addition(driver):
    calculator = SlowCalculatorPage(driver)

    # Set the delay to 45 seconds
    calculator.set_delay(45)

    # Perform the addition 7 + 8
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    # Wait for the result to be displayed
    calculator.wait_for_result(15)

    # Get the result and assert it
    result = calculator.get_result()
    assert result == '15', f"Expected result to be '15', but got '{result}'"
