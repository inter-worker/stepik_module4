from .locators import BasketPageLocators
from .base_page import BasePage
from selenium import webdriver


class BasketPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_CONTAINER), \
           "Mistake. Products are in the shopping cart" 
           
    def should_be_text_cart_is_empty(self):
        # реализуйте проверку, что есть текст о том что корзина пустая
        #tt = self.is_element_present(*BasketPageLocators.BASKET_TEXT_CART_EMPTY).text
        #tt = self.find_element_by_css_selector(*BasketPageLocators.BASKET_TEXT_CART_EMPTY).text
        
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT_CART_EMPTY), "Text 'Your shopping cart is empty' is not presented"       
