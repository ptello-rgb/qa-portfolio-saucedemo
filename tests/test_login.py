def test_login_success(my_page):
    # abre la página de login
    my_page.goto("https://www.saucedemo.com/")

    # ingresa credenciales válidas
    my_page.fill('[data-test="username"]', "standard_user")
    my_page.fill('[data-test="password"]', "secret_sauce")

    # hace click en el botón de login
    my_page.click('[data-test="login-button"]')

    # valida que el login haya llevado al inventario
    assert "inventory" in my_page.url


def test_login_invalid(my_page):
    # abre la página de login
    my_page.goto("https://www.saucedemo.com/")

    # ingresa usuario válido, pero password incorrecta
    my_page.fill('[data-test="username"]', "standard_user")
    my_page.fill('[data-test="password"]', "wrong_password")

    # intenta iniciar sesión
    my_page.click('[data-test="login-button"]')

    # toma el texto visible del mensaje de error
    error_message = my_page.locator('[data-test="error"]').inner_text()

    # valida que el mensaje corresponda a credenciales incorrectas
    assert "do not match" in error_message