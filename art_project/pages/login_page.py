
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

class Login_page(Base):

    base_url = 'https://www.artlebedev.ru/'
    email = 'mewessound@gmail.com'
    password = 'IBo0PNJGL'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    cookie_button = '//button["Прекрасно"]'
    login_page = '//a[@class="als-header-2021-nav-item als-header-2021-buttons-login"]'
    login_page_word = '//h2["Вход"]'
    email_field = '//input[@type="email"]'
    password_field = '//input[@type="password"]'
    login_button = '//button[@type="submit"]'
    main_word_main_page = '//div[@class="als-header-2023-logo"]'


# Getters

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    def get_login_page(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.login_page)))

    def get_login_page_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.login_page_word)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.XPATH, self.main_word_main_page)))


# Actions

    def click_cookie_button(self):
        self.get_cookie_button().click()
        print('Click Cookie button')

    def open_login_page(self):
        self.get_login_page().click()
        print('Open login page')

    def input_email(self, email_field):
        self.get_email_field().send_keys(email_field)
        time.sleep(1)
        print('Input email')

    def input_password(self, password_field):
        self.get_password_field().send_keys(password_field)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        time.sleep(1)
        print('Click login button')
        print('Opened main page')


# Methods

    def authorization(self):

        Logger.add_start_step(method='authorization')
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_cookie_button()
        self.open_login_page()
        self.read_word(self.get_login_page_word())
        self.assert_word(self.get_login_page_word(), 'Вход')
        self.input_email(self.email)
        self.input_password(self.password)
        self.click_login_button()
        self.read_word(self.get_main_word())
        Logger.add_end_step(url=self.driver.current_url, method='authorization')
