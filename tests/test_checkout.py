def test_checkout_flow(logged_in_page):
    # usa una página ya logueada y ubicada en inventory
    logged_in_page.click("text=Add to cart")

    # entra al carrito
    logged_in_page.click(".shopping_cart_link")

    # inicia el proceso de checkout
    logged_in_page.click("text=Checkout")

    # completa los datos requeridos del checkout
    logged_in_page.fill('[data-test="firstName"]', "Test")
    logged_in_page.fill('[data-test="lastName"]', "User")
    logged_in_page.fill('[data-test="postalCode"]', "1234")

    # continúa al resumen de compra
    logged_in_page.click('[data-test="continue"]')

    # valida que llegó al segundo paso del checkout
    assert "checkout-step-two" in logged_in_page.url