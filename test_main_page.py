from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import math
import os 
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

#def go_to_login_page(browser):
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()
    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #browser.get(link)
    #go_to_login_page(browser) 
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()   

#def test_guest_the_login_page_opens(browser):
 #   link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
 #   #browser.get(link)
  #  #go_to_login_page(browser) 
  #  page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор  экземпляр драйвера и url адрес 
  #  page.open()                      # открываем страницу
  #  page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    
  #  page.should_be_login_page()
    
    
if __name__ == "__main__":
    test_guest_can_go_to_login_page(browser)
    print("All tests passed!")    