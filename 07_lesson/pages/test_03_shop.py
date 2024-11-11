from selenium import webdriver
import pytest
from shoppage import ShoppingCartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    driver.get("https://www.saucedemo.com/")
    shopping_cart_page = ShoppingCartPage(driver)

    shopping_cart_page.login("standard_user", "secret_sauce")

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    shopping_cart_page.add_products_to_cart(products)
    shopping_cart_page.go_to_cart()

    shopping_cart_page.checkout("Kristina", "Kalaburdina", "250011")

    total_text = shopping_cart_page.get_total()
    assert total_text == "Total: $58.29"

    shopping_cart_page.complete_purchase()
