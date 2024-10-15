from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 40)

driver.get("http://uitestingplayground.com/textinput?")

name_button = driver.find_element(By.ID, "newButtonName")
name_button.send_keys("SkyPro")

submit_button = driver.find_element(By.ID, "updatingButton")
submit_button.click()

waiter.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"),
                                              "SkyPro"))

button_text = submit_button.text

print(button_text)

driver.quit()
