from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)

    def fill_form(self, fields):
        for field_name, value in fields.items():
            field = self.waiter.until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
            field.send_keys(value)

    def click_submit(self):
        submit_button = self.waiter.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()
