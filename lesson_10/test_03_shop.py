import pytest
from selenium import webdriver
from shoppage import ShoppingCartPage
import allure


@pytest.fixture(scope="function")
def driver() -> webdriver.Chrome:
    """Инициализация WebDriver для тестов.”
    Создает и настраивает экземпляр Chrome WebDriver.

        :return: Экземпляр WebDriver (Chrome).
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест корзины покупок")
@allure.description("Проверка функциональности корзины покупок на сайте.")
@allure.feature("Покупка товаров")
def test_shopping_cart(driver):
    """Тест процесса покупок на сайте."""
    driver.get("https://www.saucedemo.com/")
    shopping_cart_page = ShoppingCartPage(driver)

    # Вход в систему
    shopping_cart_page.login("standard_user", "secret_sauce")

    # Список продуктов для добавления в корзину
    products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt",
                "sauce-labs-onesie"]

    # Добавление продуктов в корзину
    shopping_cart_page.add_products_to_cart(products)
    shopping_cart_page.go_to_cart()

    # Оформление заказа
    shopping_cart_page.checkout("Kristina", "Kalaburdina", "250011")

    # Получение общей суммы и проверка её правильности
    total_text = shopping_cart_page.get_total()
    assert total_text == "Total: $58.29", (
        f"Ожидалась сумма: Total: $58.29, но получено: {total_text}"
    )

    # Завершение покупки
    shopping_cart_page.complete_purchase()
