import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class RegressionTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_carrito_funciona(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(carrito.text, "1", "El carrito no muestra el número correcto de productos.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()