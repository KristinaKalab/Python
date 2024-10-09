from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()

try:
    # Шаг 1: Откройте страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    sleep(2)

    # Шаг 2: Нажмите на кнопку "Close" в модальном окне
    close_button = driver.find_element(By.CSS_SELECTOR,
                                       "div[class='modal-footer']")
    close_button.click()

    sleep(2)

finally:
    driver.quit()
