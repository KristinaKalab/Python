from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()

try:
    # Шаг 1: Откройте страницу
    driver.get("http://the-internet.herokuapp.com/login")

    sleep(2)

    # Шаг 2: Найдите поле username по CSS-селектору и введите значение
    # "tomsmith"
    username_field = driver.find_element(By.CSS_SELECTOR, "input#username")
    username_field.send_keys("tomsmith")

    # Шаг 3: Найдите поле password по CSS-селектору и введите значение
    # "SuperSecretPassword!"
    password_field = driver.find_element(By.CSS_SELECTOR, "input#password")
    password_field.send_keys("SuperSecretPassword!")

    # Шаг 4: Найдите кнопку Login и нажмите на неё
    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button[class='radius']")
    login_button.click()

    sleep(4)

finally:
    driver.quit()
