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
    