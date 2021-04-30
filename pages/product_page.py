from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_page_click_add_to_cart_button(self):
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_CART)
        button_cart.click()
        
        
       