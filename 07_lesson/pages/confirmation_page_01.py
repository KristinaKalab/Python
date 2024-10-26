from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)

    def get_zip_code_color(self):
        zip_code_element = self.waiter.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        return zip_code_element.value_of_css_property('background-color')

    def get_background_color(self, field_id):
        field = self.waiter.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return field.value_of_css_property('background-color')
