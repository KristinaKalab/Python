from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

try:
    # Шаг 1: Откройте страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Шаг 2: Кликните на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR,
                                      "button[class='btn btn-primary']")
    blue_button.click()

    sleep(5)

finally:
    driver.quit()
