from selenium import webdriver

# Укажите путь к geckodriver, который находится в папке вашего проекта
geckodriver_path = 'C:/Users/user/Desktop/Учеба/Python/Python/geckodriver.exe'

# Создайте экземпляр веб-драйвера Firefox с указанным путем к geckodriver
driver = webdriver.Firefox()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()
