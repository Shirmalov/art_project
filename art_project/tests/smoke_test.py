
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import Login_page
from pages.store_page import Store_page
from pages.book_page import Book_page
from pages.accessories_page import Accessories_page
from pages.toys_page import Toys_page
from pages.wish_page import Wish_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page
from pages.cancellations_page import Cancellations_page

def test_select_items():
    driver = webdriver.Chrome()
    print('Start test')
    print('First part of the test:')
    lp = Login_page(driver)
    lp.authorization()

    print('---- ---- ---- ---- ----')
    print('Second part of the test:')
    mp = Store_page(driver)
    mp.store()
    
    print('---- ---- ---- ---- ----')
    print('Third part of the test:')
    bp = Book_page(driver)
    bp.select_books()
    
    print('---- ---- ---- ---- ----')
    print('Fourth part of the test:')
    ap = Accessories_page(driver)
    ap.select_accessories()
    
    print('---- ---- ---- ---- ----')
    print('Fifth part of the test:')
    tp = Toys_page(driver)
    tp.select_toys()
    
    print('---- ---- ---- ---- ----')
    print('Six part of the test:')
    wp = Wish_page(driver)
    wp.compare_wishlist_price()
    
    print('---- ---- ---- ---- ----')
    print('Seven part of the test:')
    cp = Cart_page(driver)
    cp.creating_an_order()
    
    print('---- ---- ---- ---- ----')
    print('Eighth part of the test:')
    pp = Payment_page(driver)
    pp.payment()
    time.sleep(3)
    
    print('---- ---- ---- ---- ----')
    print('Ninth part of the test:')
    canp = Cancellations_page(driver)
    canp.cancellation()

    print('Finish Test!')
