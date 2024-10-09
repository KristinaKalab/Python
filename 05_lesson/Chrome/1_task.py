from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    # Шаг 1: Откройте страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Шаг 2: Пять раз кликните на кнопку Add Element
    add_element_button = driver.find_element(By.CSS_SELECTOR,
                                             "button[onclick='addElement()']")
    for _ in range(5):
        add_element_button.click()

    # Шаг 3: Соберите со страницы список кнопок Delete
    delete_buttons = driver.find_elements(By.CSS_SELECTOR,
                                          "button[onclick='deleteElement()']")

    # Шаг 4: Выведите на экран размер списка
    print("Количество кнопок Delete:", len(delete_buttons))

finally:
    sleep(5)
    driver.quit()
