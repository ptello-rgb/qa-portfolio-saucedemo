def test_add_to_cart(logged_in_page):
    # usa una página ya logueada y ubicada en inventory
    logged_in_page.click("text=Add to cart")

    # entra al carrito
    logged_in_page.click(".shopping_cart_link")

    # valida que la navegación haya llegado al carrito
    assert "cart" in logged_in_page.url