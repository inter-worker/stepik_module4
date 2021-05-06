import math
import os 
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time
from selenium.common.exceptions import NoAlertPresentException

@pytest.mark.user_addtobasket
class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_product_in_basket_opened_from_product_page(browser):   
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
        page.open() 
        page.go_to_basket_page()
        time.sleep(1)
        basket_page = BasketPage(browser, browser.current_url)
    
        basket_page.should_not_be_success_message()      #Ожидаем, что в корзине нет товаров
        basket_page.should_be_text_cart_is_empty()        #Ожидаем, что есть текст о том что корзина пуста  

    def test_user_can_add_product_to_basket(browser, link):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.product_page_click_add_to_cart_button()
        time.sleep(1)
        page.solve_quiz_and_get_code()
        time.sleep(1)
        page.name_product()
        page.price_product()

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

    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):   
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()  
    page.go_to_basket_page()
    time.sleep(1)
    
    basket_page = BasketPage(browser, browser.current_url)
    
    basket_page.should_not_be_success_message()      #Ожидаем, что в корзине нет товаров
    basket_page.should_be_text_cart_is_empty()        #Ожидаем, что есть текст о том что корзина пуста  

def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.product_page_click_add_to_cart_button()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.name_product()
    page.price_product()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()  

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()    
    
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