# test cases

## TC-01: valid login

**requirement:** req-01  
**type:** automated UI functional test  
**priority:** high  

**steps:**
1. open SauceDemo login page.
2. enter valid username.
3. enter valid password.
4. click login.

**expected result:**  
User is redirected to the inventory page.

**automated test:**  
`tests/test_login.py::test_login_success`

---

## TC-02: invalid login

**requirement:** req-02  
**type:** automated UI functional test  
**priority:** high  

**steps:**
1. open SauceDemo login page.
2. enter valid username.
3. enter invalid password.
4. click login.

**expected result:**  
An error message is displayed.

**automated test:**  
`tests/test_login.py::test_login_invalid`

---

## TC-03: inventory loaded

**requirement:** req-03  
**type:** automated UI functional test  
**priority:** high  

**steps:**
1. log in with valid credentials.
2. open inventory page.

**expected result:**  
At least one product is displayed.

**automated test:**  
`tests/test_inventory.py::test_inventory_loaded`

---

## TC-04: add product to cart

**requirement:** req-04, req-05  
**type:** automated UI functional test  
**priority:** high  

**steps:**
1. log in with valid credentials.
2. add a product to cart.
3. open shopping cart.

**expected result:**  
User is redirected to the cart page.

**automated test:**  
`tests/test_cart.py::test_add_to_cart`

---

## TC-05: checkout flow

**requirement:** req-06  
**type:** automated UI functional test  
**priority:** high  

**steps:**
1. log in with valid credentials.
2. add a product to cart.
3. open shopping cart.
4. click checkout.
5. complete checkout information.
6. click continue.

**expected result:**  
User reaches the checkout overview page.

**automated test:**  
`tests/test_checkout.py::test_checkout_flow`