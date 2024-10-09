from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()

try:
    # Шаг 1: Откройте страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    sleep(2)

    # Шаг 2: Найдите поле ввода по CSS-селектору и введите текст "1000"
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("1000")

    sleep(2)

    # Шаг 3: Очистите поле
    input_field.clear()

    sleep(2)

    # Шаг 4: Введите текст "999" в это же поле
    input_field.send_keys("999")

    sleep(2)

finally:
    driver.quit()
