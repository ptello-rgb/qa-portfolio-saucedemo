import pytest
from playwright.sync_api import sync_playwright


# fixture base: crea una página nueva para cada test
@pytest.fixture(scope="function")
def my_page():
    with sync_playwright() as p:
        # levanta chromium en modo headless para que el test corra sin abrir ventana
        browser = p.chromium.launch(headless=True)

        # crea una nueva pestaña/página dentro del navegador
        page = browser.new_page()

        # entrega la página al test que la necesite
        yield page

        # cuando termina el test, cierra el navegador
        browser.close()


# fixture reutilizable: deja la página ya logueada
@pytest.fixture
def logged_in_page(my_page):
    my_page.goto("https://www.saucedemo.com/")

    # credenciales válidas de saucedemo
    my_page.fill('[data-test="username"]', "standard_user")
    my_page.fill('[data-test="password"]', "secret_sauce")
    my_page.click('[data-test="login-button"]')

    # validación rápida para asegurar que el login funcionó
    assert "inventory" in my_page.url

    # devuelve la misma página, pero ahora ya autenticada
    return my_page