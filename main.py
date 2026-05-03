from pages.initial_page import InitialPage
from pages.patrice_page import PatricePage
from pages.test_exceptions import TestExceptions
from pages.click_test import ClickTest


from playwright.sync_api import sync_playwright
import time

time_stamp = 2
url = 'https://practicetestautomation.com/'
patrice_page_selector = '#menu-item-20'
selector_test = "//a[text()='Test Exceptions']"
click_test_selector  = '#add_btn'
test_selector_final  = '#row2 .input-field'


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    initial_page = InitialPage(page, url)
    initial_page.home_page()

    time.sleep(time_stamp)
    patrice_page = PatricePage(page, patrice_page_selector)
    patrice_page.patrice_page()

    time.sleep(time_stamp)
    test_exceptions = TestExceptions(page,selector_test)
    test_exceptions.test_exceptions()

    time.sleep(time_stamp)
    click_test = ClickTest(page, click_test_selector, test_selector_final)
    click_test.click_test()

    time.sleep(time_stamp)
    browser.close()