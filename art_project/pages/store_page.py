
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

class Store_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    mag_store_page = '(//a[@class="als-header-2021-nav-item"])[4]'


# Getters

    def get_mag_store_page(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.mag_store_page)))


# Actions

    def open_mag_store_page(self):
        self.get_mag_store_page().click()
        print('Open "Magazinus" store page')


# Methods

    def store(self):
        Logger.add_start_step(method='store')
        self.open_mag_store_page()
        self.get_current_url()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='store')