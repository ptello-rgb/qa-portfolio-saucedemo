def test_inventory_loaded(logged_in_page):
    # usa una página ya logueada y ubicada en inventory
    items = logged_in_page.locator(".inventory_item")

    # valida que el inventario tenga al menos un producto visible
    assert items.count() > 0