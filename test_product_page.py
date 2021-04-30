import math
import os 
import pytest
from .pages.product_page import ProductPage
import time
from selenium.common.exceptions import NoAlertPresentException



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.product_page_click_add_to_cart_button()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    