import math
import os 
import pytest
from .pages.product_page import ProductPage
import time
from selenium.common.exceptions import NoAlertPresentException

#@pytest.mark.parametrize('link', ["okay_link",
#                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
#                                  "okay_link"])
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def AAAAAAAAAtest_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
   
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.product_page_click_add_to_cart_button()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.name_product()
    page.price_product()
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.product_page_click_add_to_cart_button()
    time.sleep(1)
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    time.sleep(1)
    page.should_not_be_success_message()
    
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open() 
    page.product_page_click_add_to_cart_button()
    time.sleep(1)
    page.should_the_element_disappears()