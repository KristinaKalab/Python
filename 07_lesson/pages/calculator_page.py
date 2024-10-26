from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 45)

    def set_delay(self, value):
        delay_field = self.waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_field.clear()
        delay_field.send_keys(value)

    def click_button(self, button):
        button_element = self.waiter.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//span[text()='{button}']"))
        )
        button_element.click()

    def get_result(self):
        result_locator = (By.CSS_SELECTOR, "#result")
        result_element = self.waiter.until(
            EC.presence_of_element_located(result_locator)
        )
        return result_element.text
