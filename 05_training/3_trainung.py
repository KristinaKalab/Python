from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.example.com")

print(f'Заголовок страницы: {driver.title}')

driver.quit()
sleep(10)
