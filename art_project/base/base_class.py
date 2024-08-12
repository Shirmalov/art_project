
import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)


    """Method read word"""

    def read_word(self, word):
        value_word = word.text
        print('Description: ' + value_word)


    """Method read numbers"""

    def read_numbers(self, numbers):
        value_numbers = numbers.text
        num_number = int(value_numbers)
        print(num_number)


    """Method asser word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Values are matches')


    """Method asser number"""
    def assert_number(self, number, result):
        assert number == result
        print('Number matches')


    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime('%d.%m.%y-%H:%M:%S')
        name_screen = 'screenshot-' + now_date + '.png'
        self.driver.save_screenshot('/Users/shirmalov/PycharmProjects/artlebedev_project/screen/' + name_screen)
        print('Screenshot done')
