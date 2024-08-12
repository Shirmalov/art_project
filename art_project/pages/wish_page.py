
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

total_price_wishlist_section = 4097

class Wish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    wishlist_section = '//a[@class="with-icon with-icon--wishlist"]'
    wishlist_word = '//h1["Желания"]'
    price_1 = '(//span[@class="price_current_RUB"])[1]'
    price_2 = '(//span[@class="price_current_RUB"])[2]'
    price_3 = '(//span[@class="price_current_RUB"])[3]'


# Getters

    def get_wishlist_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.wishlist_section)))

    def get_wishlist_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.wishlist_word)))

    def get_price_1(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_1)))

    def get_price_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_2)))

    def get_price_3(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_3)))


# Actions

    def open_wishlist_section(self):
        self.get_wishlist_section().click()
        print('Open Wishlist section')

    def read_prices(self):
        value_price_1 = self.get_price_1().text
        value_price_2 = self.get_price_2().text
        value_price_3 = self.get_price_3().text
        vp1 = int(value_price_1.replace('$', ''))
        vp2 = int(value_price_2.replace('$', ''))
        vp3 = int(value_price_3.replace('$', ''))
        expected_price = vp1 + vp2 + vp3
        print('Total price: ' + str(expected_price))
        assert expected_price == total_price_wishlist_section
        print('Prices are the same')


# Methods

    def compare_wishlist_price(self):

        Logger.add_start_step(method='compare_wishlist_price')
        self.open_wishlist_section()
        self.get_current_url()
        self.read_prices()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='compare_wishlist_price')
