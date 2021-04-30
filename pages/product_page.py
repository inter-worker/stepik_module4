from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_page_click_add_to_cart_button(self):
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_CART)
        button_cart.click()
        
    def name_product(self):
        name_product_text = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text  
        name_product_in_cart_text = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_CART).text
        print(name_product_text)
        print(name_product_in_cart_text)
        assert name_product_text == name_product_in_cart_text, "Name product not in add name into cart"
        
    def price_product(self):
        price_product_text = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_product_in_cart_text = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_CART).text        
        print(price_product_text)
        print(price_product_in_cart_text)
        assert price_product_text == price_product_in_cart_text, "Price product not in add price into cart"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"   
       
    def should_the_element_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Element didn't disappear"  