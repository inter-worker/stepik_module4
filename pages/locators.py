from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FORM_LOGIN_FORM = (By.ID, "login_form")
    FORM_LOGIN_EMAIL = (By.NAME, "login-username")
    FORM_LOGIN_PASS = (By.NAME, "login-password")
    FORM_LOGIN_BUTTON = (By.NAME, "login_submit")
    FORM_REGISTRATION_FORM = (By.ID, "register_form")
    FORM_REGISTRATION_EMAIL = (By.NAME, "registration-email")
    FORM_REGISTRATION_PASS = (By.NAME, "registration-password1")
    FORM_REGISTRATION_REENTERPASS = (By.NAME, "registration-password2")
    FORM_REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    
class ProductPageLocators ():
    BUTTON_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")      
    NAME_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".alertinner  > strong:nth-child(1)")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")   
    PRICE_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".alertinner p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")     