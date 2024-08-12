
import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#  Locators

    cart = '(//div[@class="cart-control js-cart-link-container"])[1]'
    button_checkout = '//button[@class="js-metrika-place-order-button pretty-button__element"]'
    checkout_word = '//h1["Оформление заказа"]'

    order = '//div[@id="orders"]/div/div/h2'
    price_1 = '(//span[@class="sum"])[3]'
    price_2 = '(//span[@class="sum"])[5]'
    price_3 = '(//span[@class="sum"])[7]'
    price_4 = '(//span[@class="sum"])[9]'
    price_5 = '(//span[@class="sum"])[11]'
    price_6 = '(//span[@class="sum"])[13]'
    price_7 = '(//span[@class="sum"])[15]'

    country_field = '//select[@class="region_widget"]'
    city_name_field = '//input[@id="city_name"]'
    select_city = '//input[@id="city"]'
    email_field = '//input[@name="email"]'
    name_last_name_field = '//input[@class="js-username"]'
    mobile_phone_field = '//input[@class="js-phone-number"]'
    postal_code_field = '//input[@class="js-postal-code"]'
    address_field = '//input[@class="js-address"]'
    comment_field = '//textarea[@class="js-comment"]'
    button_next = '//button[@class="js-metrika-choose-pay-button pretty-button__element"]'

    the_total_cost_word = '(//h2["Итоговая стоимость"])[2]'

    cost_of_goods_field = '(//td["Стоимость товаров"])[1]'
    cost_of_goods_value = '(//span[@class="sum"])[17]'

    cost_of_delivery_field = '(//td["Доставка"])[5]'
    cost_of_delivery_value = '(//span[@class="sum"])[18]'

    amount_to_be_paid_field = '(//th["Сумма к оплате:"])[1]'
    amount_to_be_paid_value = '(//span[@class="sum"])[19]'

    checkbox = '//label[@for="input-want_letters1"]'


# Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def get_checkout_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.checkout_word)))

    def get_order(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.order)))

    def get_price_1(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_1)))

    def get_price_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_2)))

    def get_price_3(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_3)))

    def get_price_4(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_4)))

    def get_price_5(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_5)))

    def get_price_6(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_6)))

    def get_price_7(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.price_7)))

    def get_country_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.country_field)))

    def get_city_name_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.city_name_field)))

    def get_select_city(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_city)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_name_last_name_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.name_last_name_field)))

    def get_name_last_name_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.name_last_name_field)))

    def get_mobile_phone_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.mobile_phone_field)))

    def get_postal_code_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.postal_code_field)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_button_next(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_next)))

    def get_the_total_cost_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.the_total_cost_word)))

    def get_cost_of_goods_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cost_of_goods_field)))

    def get_cost_of_goods_value(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cost_of_goods_value)))

    def get_cost_of_delivery_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cost_of_delivery_field)))

    def get_cost_of_delivery_value(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cost_of_delivery_value)))

    def get_amount_to_be_paid_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.amount_to_be_paid_field)))

    def get_amount_to_be_paid_value(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.amount_to_be_paid_value)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))


# Actions

    def open_cart(self):
        self.get_cart().click()
        print('Open Cart')

    def open_checkout_page(self):
        self.get_button_checkout().click()
        print('Open Checkout page')

    def open_drop_down_list_and_select_country(self):
        self.get_country_field().click()
        time.sleep(1)
        select = Select(self.get_country_field())
        select.select_by_value('238')
        print('Open drop down list')
        print('Select country: "Россия"')

    def enter_in_the_field_city(self):
        self.get_city_name_field().send_keys(' ')
        self.get_city_name_field().clear()
        self.get_city_name_field().send_keys('Арзамас')
        self.get_checkout_word().click()
        time.sleep(2)
        print('Select city: "Арзамас"')

    def enter_in_the_phone_field(self):
        self.get_mobile_phone_field().send_keys('+74959261800')
        print('Add phone number: "+74959261800"')

    def enter_in_the_postal_code_field(self):
        self.get_postal_code_field().send_keys('703765')
        print('Add postal code: "703765"')

    def enter_in_the_address_field(self):
        self.get_address_field().send_keys('Южное Шоссе, 33')
        print('Add address: "Южное Шоссе, 33"')

    def enter_in_the_comment_field(self):
        self.get_comment_field().send_keys('Отправить заказ одной посылкой')
        print('Add comment: "Отправить заказ одной посылкой"')

    def enter_in_the_name_last_name_field(self):
        self.get_name_last_name_field().send_keys(' ')
        time.sleep(1)
        self.get_name_last_name_field().clear()
        self.get_name_last_name_field().send_keys('Ivan Ivanov')
        print('Add full name: "Ivan Ivanov"')

    def enter_in_the_email_field(self):
        self.get_email_field().send_keys(' ')
        time.sleep(1)
        self.get_email_field().send_keys(Keys.COMMAND + 'a')
        self.get_email_field().send_keys(Keys.DELETE)
        self.get_email_field().send_keys('test@mail.com')
        print('Add email: "test@mail.com"')

    def compare_cart_prices(self):
        value_price_1 = self.get_price_1().text
        value_price_2 = self.get_price_2().text
        value_price_3 = self.get_price_3().text
        value_price_4 = self.get_price_4().text
        value_price_5 = self.get_price_5().text
        value_price_6 = self.get_price_6().text
        value_price_7 = self.get_price_7().text

        vp1 = int(value_price_1.replace('$', ''))
        vp2 = int(value_price_2.replace('$', ''))
        vp3 = int(value_price_3.replace('$', ''))
        vp4 = int(value_price_4.replace('$', ''))
        vp5 = int(value_price_5.replace('$', ''))
        vp6 = int(value_price_6.replace('$', ''))
        vp7 = int(value_price_7.replace('$', ''))
        expected_price = vp1 + vp2 + vp3 + vp4 + vp5 + vp6 + vp7
        print('Expected total price: ' + str(expected_price))

        actual_price = self.get_cost_of_goods_value().text
        print('Actual total price: ' + actual_price)
        assert str(expected_price) == actual_price
        print('Prices are the same')

    def compare_cart_price_including_shipping(self):
        value_full_cost = self.get_cost_of_goods_value().text
        value_cost_delivery = self.get_cost_of_delivery_value().text
        print('Cost of delivery: ' + value_cost_delivery)

        vfc = int(value_full_cost.replace('$', ''))
        vcd = int(value_cost_delivery.replace('$', ''))
        full_expected_price = vfc + vcd
        print('Full expected total price: ' + str(full_expected_price))

        full_actual_price = self.get_amount_to_be_paid_value().text
        print('Full actual total price: ' + full_actual_price)
        assert str(full_expected_price) == full_actual_price
        print('Prices are the same')


    def click_button_next(self):
        self.get_button_next().click()
        print('Click button next')

    def click_checkbox(self):
        self.get_checkbox().click()
        print('Checkbox enabled')


# Methods

    def creating_an_order(self):

        Logger.add_start_step(method='creating_an_order')
        self.open_cart()
        self.open_checkout_page()
        self.get_current_url()
        self.read_word(self.get_checkout_word())
        self.assert_word(self.get_checkout_word(), 'Оформление заказа')
        self.get_screenshot()

        self.open_drop_down_list_and_select_country()
        self.enter_in_the_field_city()
        self.enter_in_the_email_field()
        self.enter_in_the_name_last_name_field()
        self.enter_in_the_phone_field()
        self.enter_in_the_postal_code_field()
        self.enter_in_the_address_field()
        self.enter_in_the_comment_field()
        self.get_screenshot()

        self.compare_cart_prices()
        self.compare_cart_price_including_shipping()

        self.click_checkbox()
        self.click_button_next()
        Logger.add_end_step(url=self.driver.current_url, method='creating_an_order')
