
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class Cancellations_page(Base):

    base_url = 'https://store.artlebedev.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    personal_card = '//a[@class="als-header-2021-nav-item als-header-2021-buttons-login"]'
    my_orders = '(//div[@class="als-login__person-nav-item"])[1]'
    my_orders_word = '//h1["Личное в Магазинусе"]'
    orders_section = '//a[@href="/profile/orders/"]'
    order = '//span[@class="pseudo js-order-toggler"]'
    button_cancel_order = '(//span[@class="pretty-button type1"])[3]'


# Getters

    def get_personal_card(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.personal_card)))

    def get_my_orders(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.my_orders)))

    def get_my_orders_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.my_orders_word)))

    def get_orders_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.orders_section)))

    def get_order(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.order)))

    def get_button_cancel_order(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_cancel_order)))


# Actions

    def open_personal_card(self):
        self.get_personal_card().click()
        print('Open personal card')

    def open_my_orders(self):
        self.get_my_orders().click()
        print('Open my orders')

    def open_orders_section(self):
        self.get_orders_section().click()
        print('Open orders section')

    def open_order(self):
        self.get_order().click()
        print('Open order')

    def click_button_cancel_order(self):
        self.get_button_cancel_order().click()
        print('Click button cancel order')
        print('Order cancelled')


# Methods

    def cancellation(self):

        Logger.add_start_step(method='cancellation')
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()

        self.open_personal_card()
        self.open_my_orders()
        self.get_current_url()
        self.read_word(self.get_my_orders_word())
        self.assert_word(self.get_my_orders_word(), 'Личное в Магазинусе')
        self.get_screenshot()

        self.open_order()
        self.click_button_cancel_order()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='cancellation')
