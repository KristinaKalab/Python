from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

driver.find_element(By.LINK_TEXT, "Donate").click()

driver.quit()
sleep(20)
