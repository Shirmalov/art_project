
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    payment_page_word = '//h1["Способ оплаты"]'
    customer_person = '//label[@for="customer-person"]'
    radiobutton_payment_card_mir = '//label[@for="PaymentOfPart1-2"]'

    the_total_cost_word = '(//h2["Итоговая стоимость"])[1]'
    cost_of_goods_value = '(//span[@class="sum"])[1]'
    cost_of_delivery_value = '(//span[@class="sum"])[2]'
    amount_to_be_paid_value = '(//span[@class="sum"])[3]'

    button_next = '(//button[@type="submit"])[1]'


# Getters

    def get_payment_page_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.payment_page_word)))

    def get_customer_person(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.customer_person)))

    def get_radiobutton_payment_card_mir(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_payment_card_mir)))

    def get_the_total_cost_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.the_total_cost_word)))

    def get_cost_of_goods_value(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cost_of_goods_value)))

    def get_ccost_of_delivery_value(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cost_of_delivery_value)))

    def get_amount_to_be_paid_value(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.amount_to_be_paid_value)))

    def get_button_next(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_next)))


# Actions

    def click_radiobutton(self):
        self.get_radiobutton_payment_card_mir().click()
        print('Click radiobutton payment card "Mir"')

    def click_button_next(self):
        self.get_button_next().click()
        print('Click button next')

    def back(self):
        self.driver.back()
        time.sleep(1)
        print('Go back to page')


# Methods

    def payment(self):

        Logger.add_start_step(method='payment')
        self.get_current_url()
        self.read_word(self.get_payment_page_word())
        self.assert_word(self.get_payment_page_word(), 'Способ оплаты')

        self.read_word(self.get_customer_person())
        self.click_radiobutton()
        self.get_screenshot()

        self.read_word(self.get_the_total_cost_word())
        self.assert_word(self.get_the_total_cost_word(), 'Итоговая стоимость')

        self.read_word(self.get_cost_of_goods_value())
        self.assert_word(self.get_cost_of_goods_value(), '6743')

        self.read_word(self.get_ccost_of_delivery_value())
        self.assert_word(self.get_ccost_of_delivery_value(), '709')

        self.read_word(self.get_amount_to_be_paid_value())
        self.assert_word(self.get_amount_to_be_paid_value(), '7452')
        self.get_screenshot()

        self.click_button_next()
        Logger.add_end_step(url=self.driver.current_url, method='payment')
