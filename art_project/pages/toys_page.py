
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

class Toys_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    toys_page = '//a[@href="/toys-games/"]'
    toys_word = '//h1["Игры и игрушки"]'

    yo_yo_cart = '(//button[@data-product-id="176502"])[2]'
    yo_yo_word = '(//a[@href="/toys-games/yoyovelocity/"])[3]'
    yo_yo_color = '//label[@for="property_176510"]'
    like_yo_yo = '(//span[@class="pseudo add-wishes js-metrika-add-to-wishes"])[1]'
    close_yo_yo_cart_button = '//div[@class="popup_close"]'

    construction_section = '//li[@class="it_construction-kits"]'
    construction_word = '//h1["Конструкторы и роботы"]'

    product_cafe_flight = '(//span[@class="product__name"])[4]'
    product_cafe_flight_name = '//h1["Модель кафе-стекляшки «Полет» из картона"]'

    playing_cards_section = '//li[@class="it_playingcard"]'
    playing_cards_word = '//h1["Игральные карты"]'

    product_cards_for_coders = '(//span[@class="product__name"])[4]'
    product_cards_for_coders_name = '//h1["Колода карт для кодеров"]'

    add_to_order_button = '//button[@class="action_default js-metrika-add-to-cart-button pretty-button__element"]'
    hide_cart = '//div[@class="shopping-cart__close js-cart-opener-control active"]'


# Getters

    def get_toys_page(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.toys_page)))

    def get_toys_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.toys_word)))

    def get_yo_yo_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.yo_yo_cart)))

    def get_yo_yo_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.yo_yo_word)))

    def get_yo_yo_color(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.yo_yo_color)))

    def get_like_yo_yo(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.like_yo_yo)))

    def get_close_yo_yo_cart_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.close_yo_yo_cart_button)))

    def get_construction_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.construction_section)))

    def get_construction_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.construction_word)))

    def get_product_cafe_flight(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.product_cafe_flight)))

    def get_product_cafe_flight_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.product_cafe_flight_name)))

    def get_playing_cards_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.playing_cards_section)))

    def get_playing_cards_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.playing_cards_word)))

    def get_product_cards_for_coders(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.product_cards_for_coders)))

    def get_product_cards_for_coders_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.product_cards_for_coders_name)))

    def get_add_to_order_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_to_order_button)))

    def get_hide_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.hide_cart)))


# Actions

    def open_toys_page(self):
        self.driver.execute_script('window.scrollTo(0, 0)')
        self.get_toys_page().click()
        print('Open toys page')

    def open_yo_yo_cart(self):
        self.driver.execute_script('window.scrollTo(0, 1900)')
        self.get_yo_yo_cart().click()
        print('Open yo-yo cart')

    def add_yo_yo_to_wishes(self):
        self.get_like_yo_yo().click()
        print('Add yo-yo to wishes')

    def close_yo_yo_cart(self):
        self.get_close_yo_yo_cart_button().click()
        print('Close yo-yo cart')

    def open_construction_section(self):
        self.driver.execute_script('window.scrollTo(0, 0)')
        self.get_construction_section().click()
        print('Open construction section')

    def open_product_cafe_flight(self):
        self.get_product_cafe_flight().click()
        print('Open "cafe flight" product card')

    def open_playing_cards_section(self):
        self.get_playing_cards_section().click()
        print('Open playing cards section')

    def open_product_cards_for_coders(self):
        self.get_product_cards_for_coders().click()
        print('Open "cards for coders" product card')

    def click_add_to_order_button(self):
        self.get_add_to_order_button().click()
        print('Product added to cart')

    def click_hide_cart(self):
        self.get_hide_cart().click()
        print('Hide cart')

    def back(self):
        self.driver.back()
        print('Go back to page')


# Methods

    def select_toys(self):

        Logger.add_start_step(method='select_toys')
        self.open_toys_page()
        self.get_current_url()
        self.read_word(self.get_toys_word())
        self.assert_word(self.get_toys_word(), 'Игры и игрушки')
        self.get_screenshot()

        self.open_yo_yo_cart()
        self.read_word(self.get_yo_yo_word())
        self.assert_word(self.get_yo_yo_word(), 'Йо-йо «Велосити»')
        self.add_yo_yo_to_wishes()
        self.close_yo_yo_cart()

        self.open_construction_section()
        self.get_current_url()
        self.read_word(self.get_construction_word())
        self.assert_word(self.get_construction_word(), 'Конструкторы и роботы')
        self.get_screenshot()

        self.open_product_cafe_flight()
        self.get_current_url()
        self.read_word(self.get_product_cafe_flight_name())
        self.assert_word(self.get_product_cafe_flight_name(), 'Модель кафе-стекляшки «Полет» из картона')
        self.click_add_to_order_button()
        self.click_hide_cart()
        self.back()

        self.open_playing_cards_section()
        self.get_current_url()
        self.read_word(self.get_playing_cards_word())
        self.assert_word(self.get_playing_cards_word(), 'Игральные карты')
        self.get_screenshot()

        self.open_product_cards_for_coders()
        self.get_current_url()
        self.read_word(self.get_product_cards_for_coders_name())
        self.assert_word(self.get_product_cards_for_coders_name(), 'Колода карт для кодеров')
        self.click_add_to_order_button()
        self.click_hide_cart()
        self.back()
        Logger.add_end_step(url=self.driver.current_url, method='select_toys')
