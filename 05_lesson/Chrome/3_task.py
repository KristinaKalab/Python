from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

try:
    # Шаг 1: Откройте страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Шаг 2: Кликните на синюю кнопку
    blue_button = driver.find_element(
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class), ' '),"
        "' btn-primary ')]")
    blue_button.click()

    sleep(2)

finally:
    driver.quit()
