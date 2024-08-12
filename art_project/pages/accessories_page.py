
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class Accessories_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    accessories_page = '(//a[@href="/accessories/"])[1]'
    accessories_page_word = '//h1["Аксессуары"]'

    case_cart = '(//button[@data-product-id="183545"])[2]'

    case_name = '(//a[@href="/accessories/cheholus/"])[3]'
    button_like_case = '(//span[@class="pseudo add-wishes js-metrika-add-to-wishes"])[1]'
    button_close_case_cart = '//div[@class="popup_close"]'

    passport_covers_section = '//li[@class="it_passport-covers"]'
    passport_covers_word = '//h1["Обложки для паспорта"]'

    passport_cover_ru_cart = '(//span[@class="product__name"])[6]'
    passport_covers_ru_name = '//h1["Обложка для паспорта «Ру»"]'
    passport_covers_ru_color = '//label[@for="property_151755"]'

    bags_section = '//li[@class="it_bags"]'
    bags_word = '//h1["Сумки"]'
    studio_bag_cart = '(//a[@href="/accessories/bags/sumka-studia/#124003"])[1]'
    studio_bag_name = '//h1["Студийная сумка"]'
    studio_bag_color = '//label[@for="property_124004"]'

    button_add_to_order = '(//button[@type="submit"])[1]'
    button_hide_cart = '//div[@class="shopping-cart__close js-cart-opener-control active"]'


# Getters

    def get_accessories_page(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.accessories_page)))

    def get_accessories_page_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.accessories_page_word)))

    def get_case_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.case_cart)))

    def get_case_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.case_name)))

    def get_button_like_case(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_like_case)))

    def get_button_close_case_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_close_case_cart)))

    def get_passport_covers_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.passport_covers_section)))

    def get_passport_covers_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.passport_covers_word)))

    def get_passport_cover_ru_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.passport_cover_ru_cart)))

    def get_passport_covers_ru_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.passport_covers_ru_name)))

    def get_passport_covers_ru_color(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.passport_covers_ru_color)))

    def get_bags_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.bags_section)))

    def get_bags_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.bags_word)))

    def get_studio_bag_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.studio_bag_cart)))

    def get_studio_bag_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.studio_bag_name)))

    def get_studio_bag_color(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.studio_bag_color)))

    def get_button_add_to_order(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_order)))

    def get_button_hide_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_hide_cart)))


# Actions

    def open_accessories_page(self):
        self.get_accessories_page().click()
        print('Open accessories page')

    def open_case_cart(self):
        self.get_case_cart().click()
        print('Open case cart')

    def add_case_to_wishes(self):
        self.get_button_like_case().click()
        print('Add case to wishes')

    def close_case_cart(self):
        self.get_button_close_case_cart().click()
        print('Close case cart')

    def open_passport_covers_section(self):
        self.get_passport_covers_section().click()
        print('Open passport covers section')

    def open_passport_cover_ru_card(self):
        self.get_passport_cover_ru_cart().click()
        print('Open passport cover "Ru" card')

    def open_bags_section(self):
        self.get_bags_section().click()
        print('Open bags section')

    def open_studio_bag_cart(self):
        self.driver.execute_script('window.scrollTo(0, 1700)')
        self.get_studio_bag_cart().click()
        print('Open studio bag cart')

    def click_button_add_to_order(self):
        self.get_button_add_to_order().click()
        print('Product added to cart')

    def click_button_hide_cart(self):
        self.get_button_hide_cart().click()
        print('Hide cart')

    def back(self):
        self.driver.back()
        time.sleep(2)
        print('Go back to page')


# Methods

    def select_accessories(self):

        Logger.add_start_step(method='select_accessories')
        self.open_accessories_page()
        self.get_current_url()
        self.read_word(self.get_accessories_page_word())
        self.assert_word(self.get_accessories_page_word(), 'Аксессуары')
        self.get_screenshot()

        self.open_case_cart()
        self.get_current_url()
        self.read_word(self.get_case_name())
        self.assert_word(self.get_case_name(), 'Чехолус')
        self.add_case_to_wishes()
        self.close_case_cart()

        self.open_passport_covers_section()
        self.get_current_url()
        self.read_word(self.get_passport_covers_word())
        self.assert_word(self.get_passport_covers_word(), 'Обложки для паспорта')
        self.get_screenshot()

        self.open_passport_cover_ru_card()
        self.get_current_url()
        self.read_word(self.get_passport_covers_ru_name())
        self.assert_word(self.get_passport_covers_ru_name(), 'Обложка для паспорта «Ру»')
        self.read_word(self.get_passport_covers_ru_color())
        self.assert_word(self.get_passport_covers_ru_color(), 'Красная')
        self.click_button_add_to_order()
        self.click_button_hide_cart()
        self.back()

        self.open_bags_section()
        self.get_current_url()
        self.read_word(self.get_bags_word())
        self.assert_word(self.get_bags_word(), 'Сумки')
        self.get_screenshot()

        self.open_studio_bag_cart()
        self.get_current_url()
        self.read_word(self.get_studio_bag_name())
        self.assert_word(self.get_studio_bag_name(), 'Студийная сумка')
        self.read_word(self.get_studio_bag_color())
        self.assert_word(self.get_studio_bag_color(), 'Бежевая')
        self.click_button_add_to_order()
        self.click_button_hide_cart()
        self.back()
        Logger.add_end_step(url=self.driver.current_url, method='select_accessories')
