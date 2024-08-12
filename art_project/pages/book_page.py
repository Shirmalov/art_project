
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class Book_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    books_page = '//a[@href="/books/"]'
    books_page_word = '//h1["Книги"]'

    web_design_section = '(//span[@class="link_text"])[5]'
    web_design_section_word = '//h1["Веб-дизайн"]'

    interface_book = '//*[@id="showcase"]/ul/li[10]/div/a/span[2]'
    button_add_book_interface_to_cart = '(//button[@data-product-id="96744"])[1]'
    button_like_players_brain_book = '//span[@data-product-id="182258"]'

    management_section = '(//span[@class="link_text"])[17]'
    management_section_word = '//h1["Менеджмент"]'

    price_filter = '//a[@href="?sort=price&order=asc"]'
    openly_book = '(//span[@class="product__name"])[1]'
    button_add_book_openly_to_cart = '(//button[@data-product-id="120255"])[1]'

    lebedev_section = '(//span[@class="link_text"])[27]'
    lebedev_section_word = '//h1["Лебедев посоветовал"]'

    steve_jobs_book = '(//span[@class="product__name"])[32]'
    steve_jobs_book_name = '//h1["Стив Джобс"]'

    button_add_to_order = '(//button[@type="submit"])[1]'
    button_hide_cart = '//div[@class="shopping-cart__close js-cart-opener-control active"]'


# Getters

    def get_books_page(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.books_page)))

    def get_books_page_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.books_page_word)))

    def get_web_design_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.web_design_section)))

    def get_web_design_section_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.web_design_section_word)))

    def get_interface_book(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.interface_book)))

    def get_button_add_book_interface_to_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_add_book_interface_to_cart)))

    def get_button_like_players_brain_book(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_like_players_brain_book)))

    def get_management_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.management_section)))

    def get_management_section_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.management_section_word)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_openly_book(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.openly_book)))

    def get_button_add_book_openly_to_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_add_book_openly_to_cart)))

    def get_lebedev_section(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.lebedev_section)))

    def get_lebedev_section_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.lebedev_section_word)))

    def get_steve_jobs_book(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.steve_jobs_book)))

    def get_steve_jobs_book_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.steve_jobs_book_name)))

    def get_button_add_to_order(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_order)))

    def get_button_hide_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_hide_cart)))


# Actions

    def open_books_page(self):
        self.get_books_page().click()
        print('Open books page')

    def open_web_design_section(self):
        self.get_web_design_section().click()
        print('Open webdesign section')

    def add_book_interface_to_cart(self):
        self.get_button_add_book_interface_to_cart().click()
        print('Add "Interface" book to cart')

    def add_players_brain_book_to_wishes(self):
        self.get_button_like_players_brain_book().click()
        print('Add "Players brain" book to wishes')

    def open_management_section(self):
        action = ActionChains(self.driver)
        scroll_to_management = self.driver.find_element(By.XPATH, '(//span[@class="link_text"])[5]')
        action.move_to_element(scroll_to_management).perform()
        self.get_management_section().click()
        print('Open management section')

    def click_price_filter(self):
        action = ActionChains(self.driver)
        scroll_to_price_filter = self.driver.find_element(By.XPATH, '//a[@href="?sort=price&order=asc"]')
        action.move_to_element(scroll_to_price_filter).perform()
        self.get_price_filter().click()
        time.sleep(1)
        print('Sort books by price')

    def add_openly_book_to_cart(self):
        self.get_button_add_book_openly_to_cart().click()
        print('Add "Openly" book to cart')

    def open_lebedev_section(self):
        action = ActionChains(self.driver)
        scroll_to_lebedev = self.driver.find_element(By.XPATH, '(//span[@class="link_text"])[27]')
        action.move_to_element(scroll_to_lebedev).perform()
        self.get_lebedev_section().click()
        print('Open Lebedev section')

    def open_book_card_steve_jobs(self):
        action = ActionChains(self.driver)
        self.driver.execute_script('window.scrollTo(0, 1900)')
        time.sleep(2)
        scroll_to_steve_jobs_book = self.driver.find_element(By.XPATH, '(//span[@class="product__name"])[32]')
        action.move_to_element(scroll_to_steve_jobs_book).perform()
        self.get_steve_jobs_book().click()
        print('Open book card "Steve Jobs"')

    def click_button_add_to_order(self):
        self.get_button_add_to_order().click()
        print('Product added to cart')

    def click_button_hide_cart(self):
        self.get_button_hide_cart().click()
        print('Hide cart')


# Methods

    def select_books(self):

        Logger.add_start_step(method='select_books')
        self.open_books_page()
        self.get_current_url()
        self.read_word(self.get_books_page_word())
        self.assert_word(self.get_books_page_word(), 'Книги')
        self.get_screenshot()

        self.open_web_design_section()
        self.get_current_url()
        self.read_word(self.get_web_design_section_word())
        self.assert_word(self.get_web_design_section_word(), 'Веб-дизайн')
        self.get_screenshot()

        self.read_word(self.get_interface_book())
        self.assert_word(self.get_interface_book(), 'Интерфейс: новые направления в проектировании компьютерных систем')
        self.add_book_interface_to_cart()
        self.add_players_brain_book_to_wishes()

        self.open_management_section()
        self.get_current_url()
        self.read_word(self.get_management_section_word())
        self.assert_word(self.get_management_section_word(), 'Менеджмент')
        self.get_screenshot()

        self.click_price_filter()
        self.read_word(self.get_openly_book())
        self.assert_word(self.get_openly_book(), 'Открыто. Как мы будем жить, работать и учиться')
        self.add_openly_book_to_cart()

        self.open_lebedev_section()
        self.get_current_url()
        self.read_word(self.get_lebedev_section_word())
        self.assert_word(self.get_lebedev_section_word(), 'Лебедев посоветовал')
        self.get_screenshot()

        self.open_book_card_steve_jobs()
        self.get_current_url()
        self.read_word(self.get_steve_jobs_book_name())
        self.assert_word(self.get_steve_jobs_book_name(), 'Стив Джобс')
        self.click_button_add_to_order()
        self.click_button_hide_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_books')
